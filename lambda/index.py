# Day02 課題2 修正後
import json
import urllib.request

def lambda_handler(event, context):
    try:
        # event から message を取り出す
        body = json.loads(event['body'])
        message = body['message']

        # FastAPIサーバーのエンドポイント
        api_url = "https://6353-35-243-233-140.ngrok-free.app/predict" 

        # APIリクエストの準備
        data = json.dumps({"message": message}).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        req = urllib.request.Request(api_url, data=data, headers=headers, method="POST")

        # APIにリクエストを送信
        with urllib.request.urlopen(req) as response:
            response_body = json.loads(response.read().decode("utf-8"))

        assistant_response = response_body.get("response", "")

        # Lambdaのレスポンス形式に合わせて返す
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "success": True,
                "response": assistant_response
            })
        }
    except Exception as error:
        print("Error:", str(error))
        return {
            "statusCode": 500,
            "body": json.dumps({"success": False, "error": str(error)})
        }

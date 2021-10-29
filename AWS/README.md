### 아키텍처
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/with-cloudtrail-example.html

* cloudtrail, cloudwatch(logGroup) - sns - lambda

* eventBridge, cloudwatch(logGroup) - sns - lambda


### 발행되는 이벤트

jq에서 파싱하듯이 Records.Sns.Message의 내용을 토대로 말아서 람다에서 사용함

```sh
{
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:ap-northeast-2:xxx:raphael_test_sns:xxxx",
            "Sns": {
                "Type": "Notification",
                "MessageId": "5a60e27a-b986-538a-95ed-bb8f26ee272c",
                "TopicArn": "arn:aws:sns:ap-northeast-2:xxx:raphael_test_sns",
                "Subject": null,
                "Message": "{\"version\":\"0\",\"id\":\"4353ca1f-137b-5036-6a9e-d29de597e84c\",\"detail-type\":\"EC2 Instance State-change Notification\",\"source\":\"aws.ec2\",\"account\":\"xxx\",\"time\":\"2021-10-29T07:05:12Z\",\"region\":\"ap-northeast-2\",\"resources\":[\"arn:aws:ec2:ap-northeast-2:xxx:instance/i-0d3db0e9d4ca3f078\"],\"detail\":{\"instance-id\":\"i-0d3db0e9d4ca3f078\",\"state\":\"stopping\"}}",
                "Timestamp": "2021-10-29T07:05:12.987Z",
                "SignatureVersion": "1",
                "Signature": "S4anNWy7S+xxxx/Pa+gixG5bAWyv4ld5AT4BcwAdE4BMSFHn6XXeFycchmpwDGjDnMLU1BWCDmPGl1NGWt3Z3jj0OeSLKNEjMPam7sM6JdmksCoi9Oaxbjpj67tNxSgu/mDe+lFxTdrNFeWTEMkPy4DQUz9YRiEHXE2KLgU40lzk+GdAu0GomH9qPBA6r/1+cAwIDLO6Ir6qD3+wAvwEqIII9nB8Cu/OmRxnv29v2dV8KaKruczJcymNQnaQ==",
                "SigningCertUrl": "https://sns.ap-northeast-2.amazonaws.com/SimpleNotificationService-xxxx.pem",
                "UnsubscribeUrl": "https://sns.ap-northeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-northeast-2:xxx:raphael_test_sns:xxxx",
                "MessageAttributes": {}
            }
        }
    ]
}

```
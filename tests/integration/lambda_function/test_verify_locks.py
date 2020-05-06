import json

from git_lfs_aws_lambda.lambda_function.handler import lambda_handler

from .create_request import request_with_body


class TestVerifyLocks:
    API_RESOURCE = '/{repoName}/info/lfs/locks/verify'

    def test_will_respond_empty(self):
        given = request_with_body(resource=TestVerifyLocks.API_RESOURCE, body={})

        response = lambda_handler(given["event"], given["context"])
        assert response["statusCode"] == 200

        actual = json.loads(response["body"])
        assert len(actual["ours"]) == 0
        assert len(actual["theirs"]) == 0

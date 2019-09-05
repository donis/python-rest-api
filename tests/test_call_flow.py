import unittest
from messagebird import Client

try:
    from unittest.mock import Mock
except ImportError:
    # mock was added to unittest in Python 3.3, but was an external library
    # before.
    from mock import Mock


class TestCallFlow(unittest.TestCase):

    def test_get_flow(self):
        http_client = Mock()
        http_client.request.return_value = '''{
  "data": [
    {
      "id": "de3ed163-d5fc-45f4-b8c4-7eea7458c635",
      "title": "Updated call flow",
      "record": false,
      "steps": [
        {
          "id": "3538a6b8-5a2e-4537-8745-f72def6bd393",
          "action": "transfer",
          "options": {
            "destination": "31611223344"
          }
        }
      ],
      "createdAt": "2017-03-06T13:34:14Z",
      "updatedAt": "2017-03-06T15:02:38Z"
    }
  ],
  "_links": {
    "self": "/call-flows/de3ed163-d5fc-45f4-b8c4-7eea7458c635"
  }
}
        '''

        call_flow = Client('', http_client).call_flow('de3ed163-d5fc-45f4-b8c4-7eea7458c635')
        http_client.request.assert_called_once_with('call-flows/de3ed163-d5fc-45f4-b8c4-7eea7458c635', 'GET', None)

        self.assertEqual('Updated call flow', call_flow.title)

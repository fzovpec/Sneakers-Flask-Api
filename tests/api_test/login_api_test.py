import unittest
import requests


API_HOST = 'http://127.0.0.1:5000/'
SUCCESSFULL_MESSAGE = '{"Result": "Successfully logged in"}\n'
VALID_USER_DATA = {
    "data": {
        "username": "sample",
        "password": "adminadmin",
        "key": "cc116608cca1f7b906e55d253395e0edbe4c147e9f5741eb77aaaf564a02f347a786c829567328ae3df477f0d6f53cb6c180773535d08a49744b0ca1770872c48f8f641287ff9f9d649b5763886533e20a3509b1903c1b05fcea2e9df7cfca1b05f3a04481adc0f40b00abfc6386ed843e66437ab3e27e2152ea00af6ea7fbf772489064add0f4d896a00add49d57ce3797e4de489e105ad98d4770ab91e819ca994be684690026ba62ab16bdd86d60eb2f5b82268c5fcd1ab8781753039deaff1f6429c098f24d1669db3792d09a549a6fbebea9e01b9ff7a1cfb647274743e241a94ff0d9d9cd2033f6fdf3f48490b253eb7b344daa89a7105bfcd9bd2591e12d8ab1aefde54a03b78d8a01547df6336c60d66294ce28a627723c4e9157bc92afa3224fdddb18ca4c6e85a51b72fbc9e60132c628a6e4f6c1b5eff89409a61c72535fa835229c14f066320c5e7c5a1f525698486e9e39a561102c8fc9b7c76400a20254d419406b9ffe87e30ddb1fd8689bd97de7eccc5368adc97ca4c2f78133d3193150b66306ca3b9e6513faca75029819d28a530608a0cc6631639c1ed59ef5b31a87a99dc4d208571452aae99bb57dd6aa2d04183e5a750547f4b52a867ef2c1a6e34baad2573c80405c83f9af6b770d4d711d125e514578aab608ee8d072050bfdc8b13332e9012fa1fe95109ff1afe9a893b293faf932d77909411f73d61c68dce4b0a6962bc5ebe812fa651f7fabe2f9c966fed932ec22daaf58ceefdbe6827177e01aca39ce22061c9f1d114c488654b11fc1a12c3ddfd978139224fbadfeddfb31202653f9d39758a4c17aab59b95c380eb3bfba21b24b4b81601e846cd5b31fb70b46cad3cd2943abb3cd1f772b721ae2d47ed3eaf9f27d13f4b5f64b8f881afb007b5193b6578934844316d8fec535bb8ecdebbac29b5d87aebd100c432f8b87ec6b3a372a3bc960653b01c982c994f37ab7edb2e7a2a82b50fb60a4f5501929ac0b4f55d7794fd52e959882e86331599c536b45afec1666e5cc0ca1f335e24fc256799b6b665e13744ecdf76c2443b462975ffd1a72a3f7ff98e87b110c7e6dab264d67cde31bae1abe73ffbad83d7d70457f5cf27a9ec3c2338c119769d45f6104182b44e9a6bf5a26de186412a6a402c0da6953b290227a0f155a5709cddb1fc259b8fd95e26406bc9d2afc1815b43e5b954ba4ab0b162eb4258099a4c3b6d3443886aad30b095d55f242c2134b1f3af32c21b20fe0dcd5ff13334031e426d16c5b30adc798f932707e16552ee69c925da3b243ec36f7482bf930899d565f4ca0d6a8b4a54b482a4deca837ceb6bfa3fdc9c89d1419e79bcac084b234260740e52cb3b6e6d734fee6eb68b1f69429a0048f3f895e37ab3b01f5045c0266bd23dabb3f474a52baacd70f6ad3a9dcf4b6577e670df5f320ca",
        "mac": "10:dd:b1:e6:03:24",
        "product_id": "4334478f-e4c2-4a08-aee6-f783c671a2d7"
    }
}


class TestLoginApi(unittest.TestCase):
    def test_login_using_json_api(self):
        session = requests.Session()
        data = {
            'type': 'login',
            'task': {}
        }
        response_text = session.post(API_HOST, json=data).text
        self.assertEqual(response_text, SUCCESSFULL_MESSAGE)

    def test_login_using_user_data(self):
        session = requests.Session()
        data = {
            'type': 'login',
            'task': {
                'data': VALID_USER_DATA
            }
        }
        response_text = session.post(API_HOST, json=data).text
        self.assertEqual(response_text, SUCCESSFULL_MESSAGE)

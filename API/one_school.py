import requests


class Oneneschool(object):
    def register_user(self, domain, authAccountId, password, name, authType='DbAuthTypeInternal', remember=False):
        return requests.post(url=domain + '/core/users',
                                json={
                                    'authAccountId': authAccountId,
                                    'password': password,
                                    'name': name,
                                    'authType': authType,
                                    'remember': remember
                                })

    def login_user(self, domain, authAccountId, password, authType='DbAuthTypeInternal'):
        return requests.post(url=domain + '/acl/auth/{authType}/{authAccountId}'.format(
            authType=authType,
            authAccountId=authAccountId
        ),
                                json={
                                    'password': password
                                })

    def get_user_info_by_id(self, domain, user_id):
        return requests.get(url=domain + '/core/users/{}'.format(user_id)).json()

    def update_user_by_id(self, domain, user_id, about, fullName, avatarId):
        return requests.patch(url=domain + '/core/users/{}'.format(user_id),
                                 json={
                                     'about': about,
                                     'fullName': fullName,
                                     'avatarId': avatarId
                                 })

    def assign_user_role(self, domain, user_id, role):
        return requests.post(url=domain + '/acl/users/{}/roles'.format(user_id),
                                json={
                                    'role': role
                                })

    def delete_user_role(self, domain, user_id, role):
        return requests.delete(url=domain + '/acl/users/{}/roles'.format(user_id),
                                  json={
                                      'role': role
                                  })

    def create_tiket(self, domain, title, discription):
        return requests.post(url=domain + '/tickets',
                                json={
                                    'title': title,
                                    'discription': discription
                                })

    def get_tiket_by_tiket_id(self, domain, tiket_id):
        return requests.post(url=domain + '/tickets/{}'.format(tiket_id))

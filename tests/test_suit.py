from API.one_school import Oneneschool
from lib.User import User
from configuration import *
from faker import Faker
import pytest, random

fake = Faker()


@pytest.fixture()
def user():
    one = Oneneschool()
    user = User()
    user.authAccountId = fake.email()
    user.password = fake.password()
    user.name = fake.name()
    create_user_response = one.register_user(domain, user.authAccountId, user.password, user.name)
    user.user_id = create_user_response.json()['userId']
    user.session_id = create_user_response.json()['sessionId']
    return user

@pytest.fixture()
def super_admin_user():
    one = Oneneschool()
    user = User()
    user.authAccountId = 'admin@hamoye.com'
    user.password = 'BQ4AT&i+o9B?zqUAVPwYUVEDcCLBsUZoDR'
    user.name = 'Test User'
    create_user_response = one.login_user(domain, user.authAccountId, user.password)
    user.user_id = create_user_response['userId']
    user.session_id = create_user_response['sessionId']
    return user


def test_create_user(user):
    assert user.user_id
    assert user.session_id


def test_get_user_by_id(user):
    one = Oneneschool()
    request = one.get_user_info_by_id(domain, user.user_id)
    assert request['id'] == user.user_id

def test_change_user_info(user):
    one = Oneneschool()
    about = fake.text()
    fullName = fake.name()
    avatarId = fake.url()
    request = one.update_user_by_id(domain, user.user_id,about, fullName, avatarId)
    assert request.status_code == 200


def test_assign_role(super_admin_user):
    one = Oneneschool()
    role = random.choice(simple_roles)
    request = one.assign_user_role(domain, user.user_id, role)
    print request.status_code
    assert 1==2
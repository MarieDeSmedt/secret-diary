from api import api
import api.models as model


def test_api_get_cust_by_name(session_make):
    response = api.get_cust_by_name("de smedt", session_make)
    assert isinstance(response, model.Customer)


def test_api_get_cust_by_id(session_make):
    response = api.get_cust_by_id(1, session_make)
    assert isinstance(response, model.Customer)


def test_api_get_all_cust(session_make):
    response = api.get_all_customer(0, 100, session_make)
    assert type(response) is list
    assert isinstance(response[0], model.Customer)


def test_api_create_cust(session_make):
    new_cust = {'name': 'test5',
                'firstname': 'test52',
                'information': 'test522',
                'creation_date': '12/12/1212'}
    customer = api.create_customer(new_cust, session_make)
    assert isinstance(customer, model.Customer)
    assert customer.name == 'test5'

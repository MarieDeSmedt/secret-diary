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
    new_cust = {'name': 'test',
                'firstname': 'test',
                'information': 'test',
                'creation_date': '12/12/1212'}
    customer = api.create_customer(new_cust, session_make)
    assert isinstance(customer, model.Customer)
    assert customer.name == 'test'
    assert customer.firstname == 'test'
    assert customer.information == 'test'


def test_api_update_cust(session_make):
    old_cust = api.get_cust_by_name("test", session_make)
    assert isinstance(old_cust,model.Customer)
    new_cust = {'name': 'up_test',
                'firstname': 'up_test',
                'information': 'up_test',
                'modification_date': '12/12/1212'}
    customer = api.update_cust_by_id(old_cust.id_customer,new_cust,session_make)
    assert isinstance(customer, model.Customer)
    assert customer.name == 'up_test'
    assert customer.firstname == 'up_test'
    assert customer.information == 'up_test'


def test_api_delete_cust(session_make):
    customer_to_delete = api.get_cust_by_name('up_test', session_make)
    assert isinstance(customer_to_delete,model.Customer)
    if customer_to_delete:
        response = api.delete_cust_by_id(customer_to_delete.id_customer,session_make)
    else:
        response ="not success"
    assert response == "Successfully deleted"
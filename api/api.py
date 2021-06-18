from fastapi import FastAPI

api = FastAPI()


# ###################   CUSTOMER    ######################################################################

@api.get("/customer/{id}")
def get_cust_by_id(customer_df,id):
    name = "name"
    firstname = "firstname"
    information = "information"
    return {'name': name, 'firstname': firstname, 'information': information }


@api.get("/customer/")
@api.post("/customer/")
@api.put("/customer/{id}")
@api.delete("/customer/{id}")
def delete_cust_by_id(customer_df, id):
    """
    delete one customer by id
    :param customer_df: dataset from customer table
    :param id: id of customer to delete
    :return:nan
    """
    return customer_df.drop(id)

# ###################   TEXT    ######################################################################

# ###################   FEELING    ######################################################################

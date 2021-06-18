from fastapi import FastAPI

api = FastAPI()


# ###################   CUSTOMER    ######################################################################
@api.get("")
def predict(input: str):
    tfidf, model = pickle.load(open('model.bin', 'rb'))
    predictions = model.predict(tfidf.transform([input]))
    label = predictions[0]
    return {'text': input, 'label': label}


@api.get("")
@api.post("")
@api.put("")
@api.delete("")
def delete_cust_by_id(customer_df,id):
    """
    delete one customer by id
    :param customer_df: dataset from customer table
    :param id: id of customer to delete
    :return:nan
    """
    return customer_df.drop(id)




# ###################   TEXT    ######################################################################

# ###################   FEELING    ######################################################################

from sqlalchemy import insert, select, update, delete
from my_webapp.db import dal

def register_user():
    data={}
    for column in dal.users.c:
        if column.key in ['id', 'created_on', 'updated_on']:
            pass
        else: 
            data[str(column.key)] = input('Enter the {}: '.format(column.key))
    ins = insert(dal.users)
    results = dal.db_session.execute(ins, [data])
    print(results.inserted_primary_key)

def get_user(user_mail):
    sel = select([dal.users])
    sel = sel.where(dal.users.c.email_address == user_mail).limit(1)
    results = dal.db_session.execute(sel).first()
    for key in results.keys():
        print(f'{key}: {results[key]}')
    return results.id

def get_all_users():
    sel = select([dal.users])
    results = dal.db_session.execute(sel)
    for user in results:
        for key in user.keys():
            print(f'{key}: {user[key]}')
        print('________________________')
    return results

def edit_user(user_mail):
    user_id = get_user(user_mail)
    print(user_id)
    data={}
    for column in dal.users.c:
        if column.key in ['id', 'created_on', 'updated_on']:
            pass
        else:
            i = input('Enter the {}: '.format(column.key))
            if i != '':
                data[str(column.key)] = i
                
    upd = update(dal.users)
    upd = upd.where(dal.users.c.id == user_id).values(data)
    results = dal.db_session.execute(upd)
    print('updated {} user'.format(results.rowcount))

def delete_user(user_mail):
    user_id = get_user(user_mail)
    de = delete(dal.users)
    de = de.where(dal.users.c.id == user_id)
    results = dal.db_session.execute(de)
    print('deleted {} user'.format(results.rowcount))


if __name__ == '__main__':
    dal.db_init('sqlite:///test.db')
    #register_user()
    get_user(input('enter email address: '))
    get_all_users()
    #edit_user(input('enter email address: '))
    #delete_user(input('enter email address: '))

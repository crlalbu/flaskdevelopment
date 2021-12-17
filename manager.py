from main import Post, app, db, User

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)

# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     cursor = dbapi_connection.cursor()
#     cursor.execute("PRAGMA foreign_keys=ON")
#     cursor.close

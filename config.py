from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={
    r'/*': {
        'origins': '*'
    }
})

db = SQLAlchemy(app)


url="http://192.168.43.88:8088/"
auth=('Lewis', 'Lewis')
urlFreepbx = "http://192.168.115.92/admin/api/api/gql"
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjcyZWQ3ODAxODg4YWJjNTk1NWNkMzgwOWE0ZjU2YzIxYjU3ZDJiOTM4NmFkNTJjMzBjYTEwODRlZGVmN2ViYzEzYjY1ODQ0MTMyMDkxY2RlIn0.eyJhdWQiOiJkZDlmOWUyZjNmOWUwYjUxMjMzZjIyMmQyZDBlYzUzY2NhODE3OTFhM2NmNTEwM2Y5MjVjZWRjN2E3NzAzMWYwIiwianRpIjoiNzJlZDc4MDE4ODhhYmM1OTU1Y2QzODA5YTRmNTZjMjFiNTdkMmI5Mzg2YWQ1MmMzMGNhMTA4NGVkZWY3ZWJjMTNiNjU4NDQxMzIwOTFjZGUiLCJpYXQiOjE2MTkwMjEzNTUsIm5iZiI6MTYxOTAyMTM1NSwiZXhwIjoxNjE5MDI0OTU1LCJzdWIiOiIiLCJzY29wZXMiOlsiZ3FsIiwicmVzdCJdfQ.BbGvKtnflFdS7JMdXcSl_5dPcy8rOSYtwO8342G1QlQ_OPVRxemNl062JOFndw808NbyWfQ4eLHnfGQnG2NYSTdBT_FP3JIG26O-qmC1s3YTlFJiI5h1LJ2_gmGTLJWYS9cQcecdLif3kSuhLGpBecNjiWGAFgB_GlcKiVxEjB4Zse5-S8J_VvmdfhZoYJPoSfp4PfTTOV6v6-39zwtTuKAnRm8LaHR1DvkyYKA5Rbl61ggKwSO2luKSofA5vfP36k9TwaqERHzO0eTMVvKTbpNZ_mrdZBfPQSaw811SUDVPcllS9dla34pq7LnypP715aQRBxyWbhLNO64BTxZARw',
  'Content-Type': 'application/json',
}


# create the DB on demand
@app.before_first_request
def create_tables():
    db.create_all()



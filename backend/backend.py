import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou5:hogwarts@stuq.ceshiren.com:23306/lagou5db?charset=utf8mb4'
db = SQLAlchemy(app)



# testcases=[]
class TestCaseFanchenlong(db.Model):
    ##定义id是个主键
    id = db.Column(db.Integer, primary_key=True)
    ###定义name 80字符长String，unique=True唯一的/unique=False可以重复的，nullable=False不能为空
    name = db.Column(db.String(80), unique=False, nullable=False)
    ## 1000字符长String，unique=False可以重复的，nullable=True可以为空
    steps = db.Column(db.String(1000), unique=False, nullable=True)

    def __repr__(self):
        return '<TestCaseFanchenlong %r>' % self.name
class TestCaseService(Resource):
    def get(self):
        name=request.args.get('name', None)
        app.logger.info({'name': name})
        if name:
            testcase=TestCaseFanchenlong.query.filter_by(name=name).first()
            return str(testcase)
        else:
            testcases = TestCaseFanchenlong.query.all()
            app.logger.info({'testcases': testcases})
            return [str(testcase) for testcase in testcases]



    def post(self):
            testcase = TestCaseFanchenlong(
                id=request.json.get("id"),
                name=request.json.get("name"),
                steps=json.dumps(request.json.get("steps"))
            )

            db.session.add(testcase)
            db.session.commit()
            # app.logger.info({"testcase":testcase})
            # app.logger.info({"testcases":testcases})
            testcases=TestCaseFanchenlong.query.all()
            return [str(testcase) for testcase in testcases]

    def put(self):
        pass

    def delete(self):

        name = request.json['name']
        #TestCaseFanchenlong.query.all()
        # for item in testcases:
        #     if item['name'] == name:
        #         testcases.remove(item)
##从数据库查  .first取第一条记录
        testcase=TestCaseFanchenlong.query.filter_by(name=name).first()
        db.session.delete(testcase)
        testcases=TestCaseFanchenlong.query.all()
        app.logger.info({'testcases': testcases})
        return [str(testcase)  for testcase in testcases]


api.add_resource(TestCaseService, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
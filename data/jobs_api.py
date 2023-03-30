import flask
from flask import jsonify, request
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'work_size', 'collaborators',
                                    'start_date', 'end_date',
                                    'is_finished', 'team_leader'
                                    ))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'job': job.to_dict(only=('job', 'work_size', 'collaborators',
                                    'start_date', 'end_date',
                                    'is_finished', 'team_leader',
                                    ))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'collaborators',
                  'is_finished', 'team_leader']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = Jobs(
        id=request.json['id'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
        team_leader=request.json['team_leader']
    )
    if db_sess.query(Jobs).filter(Jobs.id == jobs.id).first():
        return jsonify({'error': 'ID already wxists'})
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})
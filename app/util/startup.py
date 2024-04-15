from app.models.company import Company
from app.models.skill import Skill
from app.models.topic import Topic
from app.models.jobtype import JobType
from app.models.user import User

from flask import Flask

from flask_sqlalchemy.model import Model
from flask_sqlalchemy import SQLAlchemy


defaultCompanies = [
    "TIAA",
    "Wells Fargo",
    "Duke",
    "Brooksource",
    "Fidelity",
    "HartFord",
]

defaultJobTypes = [
    "Internship",
    "CO-OP",
    "Temporary",
    "Full-Time",
    "Part-Time",
]

defaultTopics = [
    "Interview",
    "Career Fair",
    "Skills",
    "Technical Interview",
    "Applying",
    "Behavioral Interview",
    "Interview Questions"
]

defaultSoftSkills = [
    "Communication",
    "Written Communication",
    "Verbal Communication",
    "Teamwork",
    "Leadership",
    "Empathy",
    "Mentoring"
]

defaultTechnicalSkills = [
    "Programming",
    "Data Structures",
    "Algorithms",
    "Mathematics",
    "Linear Algebra",
    "Embedded Systems",
    "SQL",
    "NoSQL",
]


def createAdmin(app: Flask, db: SQLAlchemy):
    config = app.config
    admin = User(
        config.get("ADMIN_UNAME"),
        config.get("ADMIN_EMAIL"),
        config.get("ADMIN_PASSWORD"),
        True
    )
    db.session.add(admin)
    db.session.commit()


def addDefaults(model: Model, defaults, db: SQLAlchemy, is_technical=False):
    if model.query.count() > 0 and not is_technical:
        return
    defaultObjects = []
    for value in defaults:
        obj = model(value)
        if isinstance(obj, Skill) and is_technical:
            print("adding tech skill to list")
            obj.is_technical = is_technical
        defaultObjects.append(obj)
    db.session.add_all(defaultObjects)
    db.session.commit()


def addAllDefaults(db):
    addDefaults(Skill, defaultSoftSkills, db)
    addDefaults(Skill, defaultTechnicalSkills, db, True)
    addDefaults(Company, defaultCompanies, db)
    addDefaults(JobType, defaultJobTypes, db)
    addDefaults(Topic, defaultTopics, db)

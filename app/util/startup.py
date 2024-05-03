import random

from app.models.company import Company
from app.models.skill import Skill
from app.models.topic import Topic
from app.models.jobtype import JobType
from app.models.user import User
from app.models.post import Post

from app.util.default_posts import forum_posts

from flask import Flask

from flask_sqlalchemy.model import Model
from flask_sqlalchemy import SQLAlchemy

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

defaultUsers = [
    User("JDoe78", "johndoe@testing.com", "password"),
    User("Jane99", "janedoe@testing.com", "password123"),
    User("mErhrmantraut", "mike@lospolloshermanos.com", "password321"),
    User("OleMunch", "ancient@fargo.com", "password213"),
    User("ShivRoy", "shiv@waystart.com", "password312"),
    User("eAlderson", "mrrobot@fsociety.com", "password"),
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


def addAllDefaults(db):
    addDefaults(Skill, defaultSoftSkills, db)
    addDefaults(Skill, defaultTechnicalSkills, db, True)
    # addDefaults(Company, defaultCompanies, db)
    addDefaults(JobType, defaultJobTypes, db)
    addDefaults(Topic, defaultTopics, db)
    # add default users
    db.session.add_all(defaultUsers)
    db.session.add_all(forum_posts)

    # add default companies
    hartford = Company("The Hartford")
    hartford.description = "The Hartford Financial Services Group, Inc., usually known as The Hartford, is a United States-based investment and insurance company. The Hartford is a Fortune 500 company headquartered in its namesake city of Hartford, Connecticut. It was ranked 160th in Fortune 500 in the year of 2020. The company's earnings are divided between property-and-casualty operations, group benefits and mutual funds."
    hartford.has_relationship_uncc = False
    hartford.website_url = "https://www.thehartford.com/careers"
    hartford.website_url_caption = "View The Hartford's Careers Page"

    wells = Company("Wells-Fargo")
    wells.description = 'Wells Fargo & Company is an American multinational financial services company with a significant global presence. The company operates in 35 countries and serves over 70 million customers worldwide. It is a systemically important financial institution according to the Financial Stability Board, and is considered one of the "Big Four Banks" in the United States, alongside JPMorgan Chase, Bank of America, and Citigroup.'
    wells.has_relationship_uncc = True
    wells.uncc_relationship_desc = "Wells Fargo is a UNCC business partner. Recruiters from Wells Fargo are often present at UNCC Career events."
    wells.website_url = "https://www.wellsfargo.com/about/careers/"
    wells.website_caption = "Visit Wells Fargo's Careers Page"

    truist = Company("Truist")
    truist.description = "Truist Financial Corporation is an American bank holding company headquartered in Charlotte, North Carolina. The company was formed in December 2019 as the result of the merger of BB&T (Branch Banking and Trust Company) and SunTrust Banks. Its bank operates 2,781 branches in 15 states and Washington, D.C., offering consumer and commercial banking, securities brokerage, asset management, mortgage, and insurance products and services. It is on the list of largest banks in the United States by assets; as of August 2023, it is the 9th largest bank with $514 billion in assets. As of January 2021, Truist Insurance Holdings is the seventh largest insurance broker in the world, with $2.27 billion in annual revenue."
    truist.has_relationship_uncc = False
    truist.website_url = "https://careers.truist.com/us/en/"
    truist.website_url_caption = "Visit Truist's Careers Page"
    db.session.add_all([hartford, wells, truist])
    db.session.commit()


# adds likes and companies to posts
def addPostDetails(db):
    posts = Post.query.all()
    companies = Company.query.all()
    users = User.query.all()
    for post in posts:
        for company in companies:
            if company.name in post.title:
                post.companies.append(company)

        for user in users:
            if random.random() > 0.3:
                post.likes.append(user)
    db.session.commit()

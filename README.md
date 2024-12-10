# Spy Cat Agency
The Spy Cat Agency (SCA) app helps streamline the management of spy cats, their missions, and assigned targets. 
The system allows the agency to hire cats, assign them missions, and manage the progress of their targets.

## Installing using GitHub
    
```bash
git clone https://github.com/RomanHlodann/spy-cat-agency.git
cd spy-cat-agency
python -m venv venv
On mac: source venv/bin/activate Windows: venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Brief explanation of an app

**Spy Cats**:
- Create, update, remove, and list spy cats.
- Breed validation for cats.

**Missions & Targets**:
- Create missions with targets in a single request.
- Assign a cat to a mission.
- Update mission and target information (e.g., Notes, Completion).
- Prevent editing of completed targets.


Link to Postman collection (You should run requests after you run server)
https://www.postman.com/telecoms-operator-51403584/workspace/test-workspace/collection/29360303-f302c725-dbfd-4d12-85c6-b7d667b9a968?action=share&creator=29360303

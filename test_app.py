import pytest
from app import app, run

# Creating a fixture for the test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_run_function(client):

    
    # Input
    inp = "50000 30 5 single owned owned engineer CA 3 10"
    
    # Call the function
    value, recommendation, score = run(inp)
    
    #assertions 
    assert value in [0, 1]
    assert score in ["Below Requirements", "Fair", "Good", "Great"]
  


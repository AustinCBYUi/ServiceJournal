import pytest
import main as main
from pytest import approx


#Calculates three answers from labor_recommend function.
def test_labor_recommend():
    assert main.Jour.labor_recommend(main.Jour, .5, 80) == \
    approx(40.0, rel=1)
    assert main.Jour.labor_recommend(main.Jour, 4, 92) == \
    approx(368, rel=1)
    assert main.Jour.labor_recommend(main.Jour, 3, 72.5) == \
    approx(217.5, rel=1)


#Only test function that will work?
def test_function():
    #Basic package
    assert main.Jour.detailing_calculator(main.Jour, 50, 10) == \
    approx(65)
    #Intermediete Package
    assert main.Jour.detailing_calculator(main.Jour, 70, 20) == \
    approx(95)
    #Performance Package
    assert main.Jour.detailing_calculator(main.Jour, 90, 30) == \
    approx(125)

pytest.main(["-v", "--tb=line", "-rN", __file__])
import unittest
from Domain.passengerClass import Passenger
from Domain.planeClass import Plane
from Infrastructure.planeRepository import PlaneRepository
tc = unittest.TestCase()

def tests():
    test_passenger()
    test_plane()
    test_repo()

def test_passenger():
    passenger1 = Passenger("Ion","Popescu",123)
    tc.assertEqual(passenger1.get_first_name(),"Ion")
    tc.assertEqual(passenger1.get_last_name(),"Popescu")
    tc.assertEqual(passenger1.get_passport_nr(),123)

    passenger1.set_first_name("Ana")
    passenger1.set_last_name("Pop")
    passenger1.set_passport_nr(23)
    tc.assertEqual(passenger1.get_first_name(),"Ana")
    tc.assertEqual(passenger1.get_last_name(),"Pop")
    tc.assertEqual(passenger1.get_passport_nr(),23)

def test_plane():
    passenger1 = Passenger("Ion", "Popescu", 123)
    passenger2 = Passenger("Ana", "Pop", 23)

    plane1 = Plane(1, "Airline1", 200, "Destination1", [passenger1, passenger2])

    tc.assertEqual(plane1.get_id(), 1)
    tc.assertEqual(plane1.get_airline(), "Airline1")
    tc.assertEqual(plane1.get_nr_seats(), 200)
    tc.assertEqual(plane1.get_destination(), "Destination1")

    passengers = plane1.get_list_of_passengers()
    tc.assertEqual(len(passengers), 2)
    tc.assertIn(passenger1, passengers)
    tc.assertIn(passenger2, passengers)

    tc.assertEqual(plane1.get_nr_of_passengers(), 2)

    tc.assertEqual(plane1.get_nr_of_passengers_with_first_name("Ion"), 1)
    tc.assertEqual(plane1.get_nr_of_passengers_with_first_name("Ana"), 1)
    tc.assertEqual(plane1.get_nr_of_passengers_with_first_name("John"), 0)

    concat_result = plane1.concat()
    tc.assertEqual(concat_result, "2Destination1")

    plane1.set_id(2)
    plane1.set_airline("Airline2")
    plane1.set_nr_seats(150)
    plane1.set_destination("Destination2")

    tc.assertEqual(plane1.get_id(), 2)
    tc.assertEqual(plane1.get_airline(), "Airline2")
    tc.assertEqual(plane1.get_nr_seats(), 150)
    tc.assertEqual(plane1.get_destination(), "Destination2")

    passenger3 = Passenger("Bob", "Johnson", 456)
    plane1.add_passenger(passenger3)

    passengers = plane1.get_list_of_passengers()
    tc.assertEqual(len(passengers), 3)
    tc.assertIn(passenger3, passengers)

    plane1.set_passengers([passenger1, passenger2])
    passengers = plane1.get_list_of_passengers()
    tc.assertEqual(len(passengers), 2)
    tc.assertIn(passenger1, passengers)
    tc.assertIn(passenger2, passengers)

def test_repo():
    repo = PlaneRepository()
    initial_planes = len(repo.get_planes())

 
    new_plane = Plane(7, "TestAir", 30, "TestDestination")
    repo.add_plane(new_plane)

    assert len(repo.get_planes()) == initial_planes + 1

    repo = PlaneRepository()
    plane_index = 1 


    repo.sort_passengers_plane(plane_index)
    sorted_passengers = repo.get_plane_index(plane_index).get_list_of_passengers()

    assert sorted_passengers == sorted(sorted_passengers, key=lambda x: x.get_last_name())
    
    repo = PlaneRepository(data=[
        Plane(1, "TestAir", 30, "TestDestination", [Passenger("John", "Doe", 123), Passenger("Jane", "Doe", 223)]),
        Plane(2, "AnotherAir", 25, "AnotherDestination", [Passenger("Alice", "Smith", 111), Passenger("Bob", "Brown", 333)]),
        Plane(3, "ThirdAir", 20, "ThirdDestination", [Passenger("Charlie", "Williams", 444), Passenger("Diana", "Williams", 555)]),
    ])

    result_planes = repo.get_planes_passport_nr_same_letters()

    assert len(result_planes) == 0 

    repo = PlaneRepository(data=[
        Plane(1, "Airline1", 30, "TestDestination"),
        Plane(2, "Airline2", 25, "TestDestination"),
        Plane(3, "Airline3", 20, "TestDestination"),
    ])

    k = 2 
    result_planes = repo.get_k_planes_same_plane_different_airlines(k)
    assert len(result_planes) == 6

    for group in result_planes:
        assert len(set(plane.get_airline() for plane in group)) == k


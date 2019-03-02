# User-stories for Week02

## Epics story 1

**<u>Epic Story 1: As a customer, I want to browse and rent a car online easily, so that I can focus on other things in life.</u>** (6 user-stories)

----

- ***US1***: As a customer, I want to be able to specify search criteria and view available cars that match the search criteria, so that I can easily find the right car for me.
  - ***Acceptance Criteria***:
    - Test – A customer can filter cars by age, preferred pick-up and drop-off locations
    - Test – A customer should see the cars that match filtered criteria.
    - Test – A customer should be able to click on one of the cars and see its details such as car type and price for each day of car rental.
    - Test - The customer’s choice is stored and the search results only shows cars which match the customer’s requirements.
  - ***Priority***: 1
  - ***Size***: 4hrs

----

- ***US2***: As a customer, I should be able to click on the search results (if any) to enter my details and further proceed with booking, so that the booking can be finalized.

  - ***Acceptance Criteria***:
    - Test – If no cars available in the time period mentioned by customer, then system results show a blank page apologizing about the inconvenience.
    - Test – After clicking on the car, text fields for additional details should pop up for the customer to enter:
      - name of the customer and age
      - license number;
      - the rental period in number of days;
      - option to purchase an insurance cover; and
      - email-address.
    - Test - System should then store the information in the database. The system should then verify the license number of the customer.
  - **Priority**: 1 
  - ***Size***: 5hrs

-----

- ***US3***: As a customer, I would like to have the option to purchase an insurance cover, so that I would be insured if unforeseen accidents occur.

  - ***Acceptance Criteria***:
    - Test – After specifying the interest to buy the cover, a new browser tab should pop up redirecting a customer to QBEI Insurances for the customer to select his/her plan.
    - Test – A customer should be redirected back to AffordbleRentals after he/she finishes with QBEI Insurances.
  - ***Priority***: 3
  - ***Size***: 2hrs

--------

- ***US4***: As a customer, I must be able to review the final price before making payment, so that I can confirm my selection.

  - ***Acceptance Criteria***:
    - Test – A customer should see the detailed net price including all calculations and taxes.
  - ***Priority***: 2
  - ***Size***: 1hr

-----

- ***US5***: As a customer, I want to be able to pay by credit card, so that I can easily enter my payment details and complete the payment.

  - ***Acceptance Criteria***:
    - Test – An external secured payment gateway should popup when the customer decides to click “PAY”.
    - Test – After the payment process is completed, the popup should close and AffordbleRentals webpage should show “PAYMENT COMPLETED” in green.
  - ***Priority***: 2
  - ***Size***: 1hr

-----

- ***US6***: As a customer, I expect to see a booking confirmation email from AfforableRental once I have made the payment, so that I can confirm the booking process is truly completed.

  - ***Acceptance Criteria***:
    - Test – The system will automatically send email to the customer detailing:
      - Booking date
      - Pickup time
      - Car information e.g. number plate, car type, color
      - Payment invoice
  - ***Priority***: 3
  - ***Size***: 1hr

## Epic story 2

**<u>Epic Story 2: As a company staff, I want to manage the system of cat information.</u>** (2 user-stories)

---

- ***US1***: As a company staff, I should be able to log in this system with a username and password, so that I can manage the car information system safely.
  - ***Acceptance Criteria***:
    - Test - The system admin can log in and log off the database system with a correct username and password.
    - Test - If the username or password is wrong, this login will be rejected.
  - ***Priority***: 1
  - ***Size***: 1hr

-----

- ***US2***: As a company staff, I should be able to enter new car information into the system, so that I can manage our car information efficiently.
  - ***Acceptance Criteria***:
    - Test - After login, the system admin can create a new car or enter new information. And following information can be entered: 
      - vehicle-type: small, medium, large, premium
      - make
      - model
      - year
      - registration number.
  - ***Priority***: 1
  - ***Size***: 2hr

## Epic story 3

**<u>Epic Story 3: As a company Manager, I want to view the reports of our car rental.</u>**

- ***US***: As a company manager,  I should be able to generate weekly reports that show a log of cars rented during the week, so that I can analyse our profits and service.
  - ***Acceptance Criteria***:
    - Test - The system can generate a weekly report, which summarize the business.
  - ***Priority***: 2
  - ***Size***: 2hr

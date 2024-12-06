# Decor Center Database Project

## ER Diagram

At this stage of the project, the ER diagram for the database was created to manage orders for the GS-studio decor center. The diagram represents a relational model consisting of six tables:

1. **Orders**:
   - Contains information about orders, including customers, mediators, and project addresses.
   - Fields:
     - `Order_ID` (PK): Unique identifier for the order.
     - `Customer_ID` (FK): Reference to the `Customers` table.
     - `Mediator_ID` (FK): Reference to the `Mediators` table (optional).
     - `City`: The city where the project is located.
     - `Address`: The project’s address.
     - `Order_Date`: The date the order was placed.

2. **Order_Details**:
   - Describes materials and details associated with each order.
   - Fields:
     - `Detail_ID` (PK): Unique identifier for the order detail.
     - `Order_ID` (FK): Reference to the `Orders` table.
     - `Material_ID` (FK): Reference to the `Materials` table.
     - `Quantity`: The quantity of the material in kilograms.
     - `Coverage_Area`: The area covered (in square meters).
     - `Price_Per_Sqm`: The cost of applying the material per square meter.
     - `Description`: A description of the finishing work (optional).

3. **Customers**:
   - Stores information about clients placing orders.
   - Fields:
     - `Customer_ID` (PK): Unique identifier for the customer.
     - `Full_Name`: Full name of the customer.
     - `Phone_Number`: Contact phone number.

4. **Mediators**:
   - Describes mediators (e.g., contractors) who represent customers.
   - Fields:
     - `Mediator_ID` (PK): Unique identifier for the mediator.
     - `Full_Name`: Full name of the mediator.
     - `Phone_Number`: Contact phone number.
     - `Company_Name`: The name of the mediator's company (optional).

5. **Materials**:
   - Stores information about construction materials.
   - Fields:
     - `Material_ID` (PK): Unique identifier for the material.
     - `Material_Name`: Name of the material.
     - `Manufacturer_ID` (FK): Reference to the `Manufacturers` table.
     - `Purchase_Price`: Purchase price per unit.
     - `Sale_Price`: Selling price per unit.

6. **Manufacturers**:
   - Stores information about material manufacturers.
   - Fields:
     - `Manufacturer_ID` (PK): Unique identifier for the manufacturer.
     - `Manufacturer_Name`: Name of the manufacturer.
     - `Country`: The country where the manufacturer is based.
     - `Website`: The manufacturer’s website.

---

### ER Diagram

Below is the ER diagram illustrating the relationships between the tables:

![ER Diagram](ER-Diagram.JPG)

---

## Logical Structure of the ER Diagram

1. **Orders and Customers**:
   - Each order is linked to a single customer (`Customer_ID`), but a customer can place multiple orders.
   - Implemented as a **one-to-many** relationship.

2. **Orders and Mediators**:
   - An order can be linked to a mediator (`Mediator_ID`), but the field is optional. 
   - A mediator can handle multiple orders.

3. **Orders and Order_Details**:
   - Each order can contain multiple details (e.g., materials and tasks).
   - Implemented as a **one-to-many** relationship.

4. **Order_Details and Materials**:
   - Each detail refers to a specific material (`Material_ID`), but one material can appear in multiple orders.
   - Implemented as a **many-to-many** relationship.

5. **Materials and Manufacturers**:
   - Each material is produced by one manufacturer (`Manufacturer_ID`), but a manufacturer can produce multiple materials.
   - Implemented as a **one-to-many** relationship.

---

## Next Steps

The next step is to generate data for all the tables using Python, save it as CSV files, and import the data into the database.

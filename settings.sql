DROP DATABASE restaurants;
DROP USER restaurantsuser;


CREATE DATABASE restaurants;
CREATE USER restaurantuser WITH PASSWORD 'restaurants';
GRANT ALL PRIVILEGES ON DATABASE restaurants TO restaurantuser;
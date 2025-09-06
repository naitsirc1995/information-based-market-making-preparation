-- Create the table
CREATE TABLE auction_supply_demand (
  price          integer PRIMARY KEY,
  total_demand   integer NOT NULL,
  bid_size       integer NOT NULL,
  ask_size       integer NOT NULL,
  total_supply   integer NOT NULL,
  filled_volume  integer NOT NULL
);

-- Insert rows
INSERT INTO auction_supply_demand
(price, total_demand, bid_size, ask_size, total_supply, filled_volume)
VALUES
(105,  2,   2, 36, 103,  2),
(104,  2,   0, 12,  67,  2),
(103, 14,  12, 18,  55, 14),
(102, 24,  10,  8,  37, 24),
(101, 29,   5, 12,  29, 29),
(100, 37,   8,  6,  17, 17),
( 99, 58,  21,  7,  11, 11),
( 98, 73,  15,  0,   4,  4),
( 97, 91,  18,  0,   4,  4),
( 96, 134, 43,  4,   4,  4),
( 95, 147, 13,  0,   0,  0);



SELECT * FROM auction_supply_demand;


with total_supply_demand AS (
SELECT
price,
SUM(bid_size) OVER (ORDER BY PRICE DESC) my_total_demand,
bid_size,
ask_size,
SUM(ask_size) OVER(ORDER BY PRICE ASC) my_total_supply
FROM auction_supply_demand)
SELECT tsd.price trading_price, LEAST(tsd.my_total_supply,tsd.my_total_demand) filled_volume
FROM total_supply_demand tsd
ORDER BY LEAST(tsd.my_total_supply,tsd.my_total_demand) DESC
LIMIT 1
;
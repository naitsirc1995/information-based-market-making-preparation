- PostgreSQL: order book L2 snapshot (from your image)

CREATE TABLE l2_snapshot (
  level      smallint PRIMARY KEY,   -- 1 = top of book
  bid_size   integer  NOT NULL,
  bid_price  numeric(10,2) NOT NULL,
  ask_price  numeric(10,2) NOT NULL,
  ask_size   integer  NOT NULL,
  CHECK (bid_price < ask_price)
);

INSERT INTO l2_snapshot (level, bid_size, bid_price, ask_price, ask_size) VALUES
(1,  5947, 28.68, 28.69, 1320),
(2,  1686, 28.67, 28.70, 1172),
(3,  1796, 28.66, 28.71, 1854),
(4,  1409, 28.65, 28.72, 1631),
(5,  1225, 28.64, 28.73, 1648),
(6,  1136, 28.63, 28.74, 1136),
(7,  9960, 28.62, 28.75, 1090),
(8,  1033, 28.61, 28.76, 1042),
(9,  1028, 28.60, 28.77, 9440),
(10, 9390, 28.59, 28.78, 1020);


SELECT

  l2.bid_size,
  l2.bid_price,
  SUM(l2.bid_size) OVER (ORDER BY l2.bid_price DESC) total_demand,
  l2.ask_size,
  l2.ask_price,
  SUM(l2.ask_size) OVER (ORDER BY l2.ask_price ASC) total_supply

FROM l2_snapshot l2;
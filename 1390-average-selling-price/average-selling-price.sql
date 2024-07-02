# Write your MySQL query statement below
select Prices.product_id,coalesce(round(sum(UnitsSold.units*Prices.price)/sum(UnitsSold.units),2),0) as average_price from Prices
Left Join UnitsSold On UnitsSold.product_id=Prices.product_id 
AND UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
Group by product_id 
Order by product_id

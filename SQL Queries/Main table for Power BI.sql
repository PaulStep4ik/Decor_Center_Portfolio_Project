with materials_manufacturers as (
	select material_id,
			material_name,
			mf.manufacturer_name,
			mf.country,
			purchase_price,
			sell_price
	from materials m join manufacturers mf on m.manufacturer_id = mf.manufacturer_id
)

select detail_id,
		od.order_id,
		material_name,
		manufacturer_name,
		country,
		purchase_price,
		sell_price,
		quantity,
		coverage_area,
		price_per_sqm
from order_details od join materials_manufacturers mm 
		on od.material_id = mm.material_id

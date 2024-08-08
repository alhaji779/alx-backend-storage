-- script to select given a condition
SELECT band_name, CASE WHEN split is NULL THEN (2022 - formed) ELSE 
(split - formed) END as lifespan from metal_bands where style like '%Glam rock%' 
 ORDER by lifespan DESC;

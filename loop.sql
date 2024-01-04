DO $$ 
DECLARE
    counter INT := 15;
BEGIN
    LOOP
        INSERT INTO Comic (comic_id, comic_name, comic_price, comic_format) 
        VALUES (counter, 'Comic ' || counter, '$' || counter * 2, 'Format ' || counter);

        counter := counter + 1;

        EXIT WHEN counter > 20;
    END LOOP;
END $$;

SELECT * FROM Comic
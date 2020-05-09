init-db:
	psql -U postgres -d reviews -a -f ./db/schema.sql

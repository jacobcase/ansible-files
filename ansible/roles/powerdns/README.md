
#Variables

* `powerdns_pg_backend` __Bool__ Causes ansible to install and configure postgresql
as the backend for powerdns.
* `powerdns_db_user` __String__ The name of the user to create in a database backend.
Defaults to "powerdns"
* `powerdns_db_host` __String__ The host that runs the database. Defaults to the same host
the role is ran on.
* `powerdns_db_pw` __String__, __Required__ Password to use for the powerdns database user.
Required if using a database backend.
* `powerdns_db_name` __String__ The name of the database that powerdns will use to store
records. Defaults to "powerdns".

#!/usr/bin/env bash
# set env variable for prod


bash -c 'export SH_USER=sh_user; export SH_PWD=sch_#3#_pwd ; export SH_HOST=localhost; export SH_DATABASE=sh_db; export SH_ENV=ENV; exec bash'

# Note: its adviced to manualy copy the env variables and set them, because executing this script creates multiple
# sub shells.

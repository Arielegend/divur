# ---------- CREATE TABLES Statements

sql_create_rateFcl_table = """ CREATE TABLE IF NOT EXISTS ratesFcl (
                                    fclRateId INTEGER PRIMARY KEY,
                                    portName text NOT NULL,
                                    portCode text NOT NULL,
                                    region text NOT NULL,
                                    state text NOT NULL,
                                    carrier text NOT NULL,                                  
                                    ratesAshdod text NOT NULL,
                                    ratesHaifa text NOT NULL,                              
                                    validFrom text NOT NULL,
                                    validUntil text NOT NULL
                                ); """

sql_create_Client_table = """ CREATE TABLE IF NOT EXISTS clients (
                                    clientId INTEGER PRIMARY KEY,
                                    firstName text NOT NULL,
                                    lastName text NOT NULL,
                                    email text NOT NULL,
                                    phone text NOT NULL,
                                    deltaFcl text NOT NULL,                                  
                                    deltaLcl text NOT NULL,
                                    deltaAir text NOT NULL,                              
                                    relevantPorts text NOT NULL,
                                    info text NOT NULL
                                ); """


sql_create_ports_table = """ CREATE TABLE IF NOT EXISTS ports (
                                    portId INTEGER PRIMARY KEY,
                                    portName text NOT NULL,
                                    portCode text NOT NULL,
                                    portState text NOT NULL,
                                    PortAliases text NOT NULL
                                ); """


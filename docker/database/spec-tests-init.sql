-- DROP TABLE credit.credit_limit_business;

CREATE SCHEMA credit;

CREATE TABLE credit.credit_limit_business (
    id UUID NOT NULL, 
    document VARCHAR(14) NOT NULL UNIQUE, 
    cgr NUMERIC(11, 2) NOT NULL, 
    qia NUMERIC(11, 2) NOT NULL, 
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX ix_credit_limit_business_document ON credit.credit_limit_business (document);

-- Drop table

-- DROP TABLE account;

CREATE TABLE account (
	id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	has_access bool NULL,
	can_transact bool NULL,
	balance numeric(10, 2) NULL,
    hold_balance numeric(10, 2) NULL,
    conciliation_balance numeric(10, 2) NULL,
	branch varchar(4) NULL,
	"number" varchar(16) NULL,
	"document" varchar(14) NOT NULL,
	"name" varchar(128) NOT NULL,
	nickname varchar(128) NULL,
	trade_name varchar(128) NULL,
	status varchar(255) NOT NULL,
	category varchar(255) NOT NULL,
	business_type varchar(255) NULL,
	business_size varchar(255) NULL,
	"password" varchar(255) NULL,
	CONSTRAINT account_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_account_can_transact ON public.account USING btree (can_transact);
CREATE INDEX ix_account_category ON public.account USING btree (category);
CREATE INDEX ix_account_document ON public.account USING btree (document);
CREATE INDEX ix_account_has_access ON public.account USING btree (has_access);
CREATE INDEX ix_account_number ON public.account USING btree (number);



-- Drop table

-- DROP TABLE "user";

CREATE TABLE "user" (
	id uuid NOT NULL,
	biometric_id uuid NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	last_login_at timestamp NULL,
	legal_terms_and_policies_accepted_at timestamp NULL,
	birth_date date NOT NULL,
	has_access bool NOT NULL,
	"document" varchar(11) NOT NULL,
	"name" varchar(128) NOT NULL,
	nickname varchar(128) NOT NULL,
	mother_name varchar(128) NULL,
	status varchar(255) NOT NULL,
	is_public_person varchar(255) NULL,
	occupation varchar(255) NULL,
	declared_income varchar(255) NULL,
	"password" varchar(255) NOT NULL,
	device_token varchar(255) NULL,
	first_access bool NOT NULL,
	public_key text NULL,
	asserted_income_currency varchar(255) NULL,
	asserted_income numeric(10, 2) NULL,
	external_response json NULL,
	CONSTRAINT user_pkey PRIMARY KEY (id)
);

INSERT INTO "user" (
    id,
    biometric_id,
    created_at,
    updated_at,
    last_login_at,
    legal_terms_and_policies_accepted_at,
    birth_date,
    has_access,
    "document",
    "name",
    nickname,
    mother_name,
    status,
    is_public_person,
    occupation,
    declared_income,
    "password",
    device_token,
    first_access,
    public_key,
    asserted_income_currency,
    asserted_income,
    external_response
) VALUES (
    '550e8400-e29b-41d4-a716-446655440001',
    NULL,
    CURRENT_TIMESTAMP,
    NULL,
    NULL,
    NULL,
    '1990-01-01',
    TRUE,
    '12345678901',
    'João da Silva',
    'joaosilva',
    'Maria da Silva',
    'active',
    NULL,
    'Desenvolvedor',
    '3000-5000',
    'hashed_password_aqui',
    NULL,
    TRUE,
    NULL,
    'BRL',
    4500.00,
    NULL
);


CREATE UNIQUE INDEX ix_user_document ON public."user" USING btree (document);


-- Drop table

-- DROP TABLE membership;

CREATE TABLE membership (
	id uuid NOT NULL,
	user_id uuid NOT NULL,
	account_id uuid NOT NULL,
	is_default bool NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	device_id varchar(256) NOT NULL,
	firebase_key varchar(256) NULL,
	phone varchar(11) NOT NULL,
	email varchar(255) NOT NULL,
	status varchar(255) NOT NULL,
	roles _varchar NULL,
	CONSTRAINT membership_account_id_user_id_key UNIQUE (account_id, user_id),
	CONSTRAINT membership_pkey PRIMARY KEY (id),
	CONSTRAINT membership_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id),
	CONSTRAINT membership_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user"(id)
);
CREATE INDEX ix_membership_phone ON public.membership USING btree (phone);
CREATE INDEX ix_membership_status ON public.membership USING btree (status);

-- Drop table

-- DROP TABLE address;

CREATE TABLE address (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	is_principal bool NULL,
	address varchar(64) NOT NULL,
	address_number varchar(8) NOT NULL,
	address_name varchar(64) NULL,
	complement varchar(32) NULL,
	neighborhood varchar(64) NOT NULL,
	city varchar(32) NOT NULL,
	state varchar(2) NOT NULL,
	zipcode varchar(8) NOT NULL,
	CONSTRAINT address_pkey PRIMARY KEY (id),
	CONSTRAINT address_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id)
);

-- Drop table

-- DROP TABLE alembic_version;

CREATE TABLE alembic_version (
	version_num varchar(32) NOT NULL,
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Drop table

-- DROP TABLE awsdms_apply_exceptions;

CREATE TABLE awsdms_apply_exceptions (
	"TASK_NAME" varchar(128) NOT NULL,
	"TABLE_OWNER" varchar(128) NOT NULL,
	"TABLE_NAME" varchar(128) NOT NULL,
	"ERROR_TIME" timestamp NOT NULL,
	"STATEMENT" text NOT NULL,
	"ERROR" text NOT NULL
);

-- Drop table

-- DROP TABLE awsdms_validation_failures_v1;

CREATE TABLE awsdms_validation_failures_v1 (
	"TASK_NAME" varchar(128) NOT NULL,
	"TABLE_OWNER" varchar(128) NOT NULL,
	"TABLE_NAME" varchar(128) NOT NULL,
	"FAILURE_TIME" timestamp NOT NULL,
	"KEY_TYPE" varchar(128) NOT NULL,
	"KEY" varchar(7800) NOT NULL,
	"FAILURE_TYPE" varchar(128) NOT NULL,
	"DETAILS" varchar(7800) NOT NULL
);

-- Drop table

-- DROP TABLE card;

CREATE TABLE card (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	is_activated bool NULL,
	is_locked bool NULL,
	is_canceled bool NULL,
	last_digits varchar(4) NULL,
	proxy varchar(128) NOT NULL,
	category varchar(255) NOT NULL,
	status varchar(255) NOT NULL,
	CONSTRAINT card_pkey PRIMARY KEY (id),
	CONSTRAINT card_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id)
);
CREATE INDEX ix_card_proxy ON public.card USING btree (proxy);

-- Drop table

-- DROP TABLE "document";

CREATE TABLE "document" (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	is_valid bool NOT NULL,
	category varchar(255) NOT NULL,
	external_status varchar(255) NOT NULL,
	"token" varchar(128) NULL,
	url varchar(128) NOT NULL,
	external_response json NULL,
	CONSTRAINT document_pkey PRIMARY KEY (id),
	CONSTRAINT document_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id)
);
CREATE INDEX ix_document_category ON public.document USING btree (category);
CREATE INDEX ix_document_external_status ON public.document USING btree (external_status);
CREATE INDEX ix_document_token ON public.document USING btree (token);

-- Drop table

-- DROP TABLE password_transaction;

CREATE TABLE password_transaction (
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	id uuid NOT NULL,
	"blocked" bool NULL,
	"password" varchar(255) NOT NULL,
	membership_id uuid NOT NULL,
	CONSTRAINT password_transaction_pkey PRIMARY KEY (id),
	CONSTRAINT password_transaction_membership_id_fkey FOREIGN KEY (membership_id) REFERENCES membership(id)
);



-- Drop table

-- DROP TABLE schedule;

CREATE TABLE schedule (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	creator_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	settle_date date NOT NULL,
	expires_on time NOT NULL,
	category varchar(255) NOT NULL,
	status varchar(255) NOT NULL,
	operation_metadata json NOT NULL,
	response_metadata json NULL,
	modified_date date NULL,
	CONSTRAINT schedule_pkey PRIMARY KEY (id),
	CONSTRAINT schedule_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id),
	CONSTRAINT schedule_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES "user"(id)
);
CREATE INDEX ix_schedule_expires_on ON public.schedule USING btree (expires_on);
CREATE INDEX ix_schedule_settle_date ON public.schedule USING btree (settle_date);
CREATE INDEX ix_schedule_status ON public.schedule USING btree (status);


-- Drop table

-- DROP TABLE payroll;

CREATE TABLE payroll (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	schedule_id uuid NULL,
	creator_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	payment_date date NOT NULL,
	reference_date date NOT NULL,
	description varchar(255) NOT NULL,
	total_amount numeric(10, 2) NULL,
	status varchar(255) NOT NULL,
	transaction_type varchar(255) NULL,
	deleted_at date NULL,
	CONSTRAINT payroll_pkey PRIMARY KEY (id),
	CONSTRAINT payroll_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id),
	CONSTRAINT payroll_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES "user"(id),
	CONSTRAINT payroll_schedule_id_fkey FOREIGN KEY (schedule_id) REFERENCES schedule(id)
);


-- Drop table

-- DROP TABLE payroll_item;

CREATE TABLE payroll_item (
	id uuid NOT NULL,
	payroll_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	bank_code varchar(3) NULL,
	account_branch varchar(4) NULL,
	account_number varchar(16) NULL,
	"document" varchar(14) NULL,
	"name" varchar(128) NULL,
	account_type varchar(255) NULL,
	amount numeric(10, 2) NULL,
	status varchar(255) NOT NULL,
	ispb_code varchar(60) NULL,
	CONSTRAINT payroll_item_pkey PRIMARY KEY (id),
	CONSTRAINT payroll_item_payroll_id_fkey FOREIGN KEY (payroll_id) REFERENCES payroll(id)
);
CREATE INDEX ix_payroll_item_account_number ON public.payroll_item USING btree (account_number);
CREATE INDEX ix_payroll_item_document ON public.payroll_item USING btree (document);

-- Drop table

-- DROP TABLE payroll_item_error;

CREATE TABLE payroll_item_error (
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	id uuid NOT NULL,
	field varchar(25) NOT NULL,
	reason varchar(255) NOT NULL,
	payroll_item_id uuid NOT NULL,
	original_value varchar(128) NULL,
	CONSTRAINT payroll_item_error_pkey PRIMARY KEY (id),
	CONSTRAINT payroll_item_error_payroll_item_id_fkey FOREIGN KEY (payroll_item_id) REFERENCES payroll_item(id)
);


-- Drop table

-- DROP TABLE pix_entry;

CREATE TABLE pix_entry (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	is_active bool NULL,
	entry varchar(255) NOT NULL,
	category varchar(255) NOT NULL,
	CONSTRAINT pix_entry_pkey PRIMARY KEY (id),
	CONSTRAINT pix_entry_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id)
);

-- Drop table

-- DROP TABLE pix_claim;

CREATE TABLE pix_claim (
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	id uuid NOT NULL,
	claim_id uuid NULL,
	"type" varchar(255) NOT NULL,
	"action" varchar(255) NOT NULL,
	status varchar(255) NOT NULL,
	previous_status varchar(255) NULL,
	reason varchar(255) NULL,
	entry_key varchar(255) NOT NULL,
	entry_key_category varchar(255) NOT NULL,
	executed_by varchar(255) NULL,
	executed_at timestamp NULL,
	claimer_branch varchar(8) NOT NULL,
	claimer_number varchar(16) NOT NULL,
	claimer_bank_ispb varchar(8) NOT NULL,
	donor_branch varchar(8) NULL,
	donor_number varchar(16) NULL,
	donor_bank_ispb varchar(8) NULL,
	claim_created_at timestamp NOT NULL,
	claim_updated_at timestamp NULL,
	resolution_limit_date timestamp NULL,
	conclusion_limit_date timestamp NULL,
	event_version varchar(255) NOT NULL,
	event_emitted_at timestamp NOT NULL,
	event_metadata json NULL,
	pix_entry_id uuid NULL,
	account_id uuid NOT NULL,
	claimer_bank_name varchar(255) NULL,
	donor_bank_name varchar(255) NULL,
	CONSTRAINT pix_claim_pkey PRIMARY KEY (id),
	CONSTRAINT pix_claim_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id),
	CONSTRAINT pix_claim_pix_entry_id_fkey FOREIGN KEY (pix_entry_id) REFERENCES pix_entry(id)
);


-- Drop table

-- DROP TABLE "transaction";

CREATE TABLE "transaction" (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	related_id uuid NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	transacted_at timestamp NOT NULL,
	is_refund bool NULL,
	can_refund bool NULL,
	amount numeric(10, 2) NOT NULL,
	balance_after numeric(10, 2) NOT NULL,
	balance_before numeric(10, 2) NOT NULL,
	description varchar(255) NULL,
	display_message varchar(255) NULL,
	entity_id varchar(128) NOT NULL,
	webhook_id varchar(128) NOT NULL,
	cash_flow varchar(255) NOT NULL,
	context varchar(255) NOT NULL,
	"event" varchar(255) NOT NULL,
	response_metadata json NOT NULL,
	idempotency_key varchar(32) NULL,
	CONSTRAINT transaction_idempotency_key_key UNIQUE (idempotency_key),
	CONSTRAINT transaction_pkey PRIMARY KEY (id),
	CONSTRAINT transaction_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id),
	CONSTRAINT transaction_related_id_fkey FOREIGN KEY (related_id) REFERENCES "transaction"(id)
);
CREATE INDEX ix_transaction_entity_id ON public.transaction USING btree (entity_id);
CREATE INDEX transacted_at ON public.transaction USING btree (transacted_at, amount);

-- Drop table

-- DROP TABLE pix_transaction_detail;

CREATE TABLE pix_transaction_detail (
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	id uuid NOT NULL,
	inicialization_type varchar(255) NOT NULL,
	addressing_key_type varchar(8) NULL,
	addressing_key_value varchar(255) NULL,
	"document" varchar(14) NOT NULL,
	"name" varchar(255) NOT NULL,
	bank_ispb varchar(16) NOT NULL,
	bank_name varchar(255) NOT NULL,
	bank_code varchar(3) NOT NULL,
	account_branch varchar(4) NOT NULL,
	account_number varchar(16) NOT NULL,
	account_type varchar(255) NOT NULL,
	transaction_id uuid NOT NULL,
	CONSTRAINT pix_transaction_detail_pkey PRIMARY KEY (id),
	CONSTRAINT pix_transaction_detail_transaction_id_fkey FOREIGN KEY (transaction_id) REFERENCES "transaction"(id)
);

-- Drop table

-- DROP TABLE pix_user_claim;

CREATE TABLE pix_user_claim (
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	id uuid NOT NULL,
	pix_claim_id uuid NOT NULL,
	user_id uuid NOT NULL,
	"action" varchar(255) NOT NULL,
	CONSTRAINT pix_user_claim_pkey PRIMARY KEY (id),
	CONSTRAINT pix_user_claim_pix_claim_id_fkey FOREIGN KEY (pix_claim_id) REFERENCES pix_claim(id),
	CONSTRAINT pix_user_claim_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user"(id)
);


-- Drop table

-- DROP TABLE device;

CREATE TABLE device (
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	id uuid NOT NULL,
	public_key text NOT NULL,
	is_active bool NULL,
	device_id varchar(256) NOT NULL,
	last_login_at timestamp NULL,
	user_id uuid NOT NULL,
	CONSTRAINT device_pkey PRIMARY KEY (id),
	CONSTRAINT device_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user"(id)
);

-- Drop table

-- DROP TABLE favorite;

CREATE TABLE favorite (
	id uuid NOT NULL,
	account_id uuid NOT NULL,
	creator_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	nickname varchar(128) NOT NULL,
	"name" varchar(128) NOT NULL,
	category varchar(255) NOT NULL,
	contact_metadata json NOT NULL,
	CONSTRAINT favorite_pkey PRIMARY KEY (id),
	CONSTRAINT favorite_account_id_fkey FOREIGN KEY (account_id) REFERENCES account(id),
	CONSTRAINT favorite_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES "user"(id)
);
CREATE INDEX ix_favorite_category ON public.favorite USING btree (category);



-- Drop table

-- DROP TABLE notification;

CREATE TABLE notification (
	id uuid NOT NULL,
	membership_id uuid NOT NULL,
	created_at timestamp NOT NULL,
	updated_at timestamp NULL,
	sent_at timestamp NOT NULL,
	title varchar(128) NULL,
	message varchar(255) NOT NULL,
	external_id varchar(64) NULL,
	"source" varchar(64) NOT NULL,
	"event" varchar(255) NOT NULL,
	route varchar(255) NOT NULL,
	CONSTRAINT notification_pkey PRIMARY KEY (id),
	CONSTRAINT notification_membership_id_fkey FOREIGN KEY (membership_id) REFERENCES membership(id) ON DELETE CASCADE
);

CREATE TABLE merchant (
    id uuid NOT NULL,
    external_id varchar(128) NULL UNIQUE,
    trading_name varchar(128) NOT NULL,
    name varchar(128) NOT NULL,
    status varchar(255) NOT NULL,
    created_at timestamp NOT NULL,
	updated_at timestamp NULL,
    CONSTRAINT merchant_pkey PRIMARY KEY (id)
);

CREATE TABLE account_merchant (
    id uuid NOT NULL,
    linked boolean DEFAULT true,
    account_id uuid NOT NULL,
    merchant_id uuid NOT NULL,
    created_at timestamp NOT NULL,
	updated_at timestamp NULL,
    CONSTRAINT account_merchant_pkey PRIMARY KEY (id),
    CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES account (id),
    CONSTRAINT fk_merchant FOREIGN KEY (merchant_id) REFERENCES merchant (id),
    CONSTRAINT account_merchant_unique UNIQUE (account_id, merchant_id)
);

-- Índices
CREATE INDEX ix_account_merchant_account_id ON public.account_merchant USING btree (account_id);
CREATE INDEX ix_account_merchant_merchant_id ON public.account_merchant USING btree (merchant_id);
CREATE INDEX ix_account_merchant_linked ON public.account_merchant USING btree (linked);

-- Drop table

-- DROP TABLE receivables_advance_proposal;

CREATE TABLE receivables_advance_proposal (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    status VARCHAR(255) NOT NULL DEFAULT 'created',
    type VARCHAR(255) NOT NULL,
    amount_requested NUMERIC(10, 2) NOT NULL,
    amount_gross NUMERIC(10, 2) NOT NULL,
    amount_net NUMERIC(10, 2) NOT NULL,
    discount_rate NUMERIC(5, 2) NOT NULL,
    discount_amount NUMERIC(10, 2) NOT NULL,
    settle_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    expires_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    merchant_id UUID NOT NULL REFERENCES merchant(id),
    created_at TIMESTAMP NOT NULL,
	updated_at TIMESTAMP NULL,
	submitted_at TIMESTAMP NULL
);

-- Drop table

-- DROP TABLE membership_receivables_advance_proposal;

CREATE TABLE membership_receivables_advance_proposal (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    action VARCHAR(255) NOT NULL DEFAULT 'created',
    membership_id UUID NOT NULL REFERENCES membership(id),
    receivables_advance_proposal_id UUID NOT NULL REFERENCES receivables_advance_proposal(id),
    created_at TIMESTAMP NOT NULL,
	updated_at TIMESTAMP NULL,
    CONSTRAINT membership_receivables_advance_proposal_unique
        UNIQUE (receivables_advance_proposal_id, action)
);

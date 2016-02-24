--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.1
-- Dumped by pg_dump version 9.5.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE event (
    eventid integer NOT NULL,
    host character varying,
    event_description character varying,
    iga_leg character varying,
    press boolean,
    press_note character varying,
    no_of_travelers integer,
    no_of_travelers_note character varying
);


ALTER TABLE event OWNER TO postgres;

--
-- Name: event_eventid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE event_eventid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE event_eventid_seq OWNER TO postgres;

--
-- Name: event_eventid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE event_eventid_seq OWNED BY event.eventid;


--
-- Name: event_loc_principal_travel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE event_loc_principal_travel (
    eventid integer,
    locationid integer,
    travelid integer,
    principalid integer
);


ALTER TABLE event_loc_principal_travel OWNER TO postgres;

--
-- Name: event_location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE event_location (
    eventid integer,
    locationid integer
);


ALTER TABLE event_location OWNER TO postgres;

--
-- Name: location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE location (
    locationid integer NOT NULL,
    city character varying,
    state character(2),
    country character varying
);


ALTER TABLE location OWNER TO postgres;

--
-- Name: location_locationid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE location_locationid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE location_locationid_seq OWNER TO postgres;

--
-- Name: location_locationid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE location_locationid_seq OWNED BY location.locationid;


--
-- Name: principal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE principal (
    principalid integer NOT NULL,
    name character varying,
    title character varying,
    agency character varying,
    principal_poc character varying
);


ALTER TABLE principal OWNER TO postgres;

--
-- Name: principal_principalid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE principal_principalid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE principal_principalid_seq OWNER TO postgres;

--
-- Name: principal_principalid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE principal_principalid_seq OWNED BY principal.principalid;


--
-- Name: principal_travel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE principal_travel (
    travelid integer,
    principalid integer
);


ALTER TABLE principal_travel OWNER TO postgres;

--
-- Name: travel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE travel (
    travelid integer NOT NULL,
    start_date date,
    end_date date,
    category character varying,
    format character varying
);


ALTER TABLE travel OWNER TO postgres;

--
-- Name: travel_travelid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE travel_travelid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE travel_travelid_seq OWNER TO postgres;

--
-- Name: travel_travelid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE travel_travelid_seq OWNED BY travel.travelid;


--
-- Name: vw_principal_travel; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW vw_principal_travel AS
 SELECT b.travelid,
    b.start_date,
    b.end_date,
    b.category,
    b.format,
    c.eventid,
    c.host,
    c.event_description,
    c.iga_leg,
    c.press,
    c.press_note,
    c.no_of_travelers,
    c.no_of_travelers_note,
    d.locationid,
    d.city,
    d.state,
    d.country,
    e.principalid,
    e.name,
    e.title,
    e.agency,
    e.principal_poc
   FROM ((((event_loc_principal_travel a
     JOIN travel b ON ((a.travelid = b.travelid)))
     JOIN event c ON ((a.eventid = c.eventid)))
     JOIN location d ON ((a.locationid = d.locationid)))
     JOIN principal e ON ((a.principalid = e.principalid)));


ALTER TABLE vw_principal_travel OWNER TO postgres;

--
-- Name: eventid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY event ALTER COLUMN eventid SET DEFAULT nextval('event_eventid_seq'::regclass);


--
-- Name: locationid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY location ALTER COLUMN locationid SET DEFAULT nextval('location_locationid_seq'::regclass);


--
-- Name: principalid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal ALTER COLUMN principalid SET DEFAULT nextval('principal_principalid_seq'::regclass);


--
-- Name: travelid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY travel ALTER COLUMN travelid SET DEFAULT nextval('travel_travelid_seq'::regclass);


--
-- Name: event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_pkey PRIMARY KEY (eventid);


--
-- Name: location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY location
    ADD CONSTRAINT location_pkey PRIMARY KEY (locationid);


--
-- Name: principal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY principal
    ADD CONSTRAINT principal_pkey PRIMARY KEY (principalid);


--
-- Name: travel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY travel
    ADD CONSTRAINT travel_pkey PRIMARY KEY (travelid);


--
-- PostgreSQL database dump complete
--


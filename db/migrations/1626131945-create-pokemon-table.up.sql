CREATE TABLE POKEMON_SPECIES (
    id INTEGER PRIMARY KEY,
    identifier VARCHAR,
    generation_id INTEGER,
    evolves_from_species_id INTEGER NULL,
    evolution_chain_id INTEGER,
    color_id INTEGER,
    shape_id INTEGER,
    habitat_id INTEGER,
    gender_rate INTEGER,
    capture_rate INTEGER,
    base_happiness INTEGER,
    is_baby BOOLEAN,
    hatch_counter INTEGER,
    has_gender_differences INTEGER,
    growth_rate_id INTEGER,
    forms_switchable INTEGER,
    is_legendary BOOLEAN,
    is_mythical BOOLEAN,
    order_prio INTEGER,
    conquest_order INTEGER NULL,

    FOREIGN KEY(evolves_from_species_id) REFERENCES POKEMON_SPECIES(id)
);

CREATE TABLE POKEMONS (
    id INTEGER PRIMARY KEY,
    identifier VARCHAR,
    species_id INTEGER,
    height INTEGER,
    weight INTEGER,
    base_experience INTEGER,
    order_prio INTEGER,
    is_default BOOLEAN,

    FOREIGN KEY(species_id) REFERENCES POKEMON_SPECIES(id)
);

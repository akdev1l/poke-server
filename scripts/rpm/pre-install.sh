#!/bin/bash

POKE_GROUP="poke-server"
POKE_USER="poke-server"
POKE_HOME="/var/lib/poke_server/jail"

if ! getent group "$POKE_GROUP" &>/dev/null; then
    groupadd --system "$POKE_GROUP"
fi

if ! getent passwd "$POKE_USER" &>/dev/null; then
    useradd --system \
        --home-dir "$POKE_HOME" \
        -g "$POKE_GROUP" \
        --create-home "$POKE_USER"
fi

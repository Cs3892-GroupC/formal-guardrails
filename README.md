# formal-guardrails
CS 3892 Group C: Formal verification of LLM policy compliance using Z3 and automated reasoning

This project investigates whether formal reasoning with Z3 can detect policy-inconsistent LLM responses more reliably than heuristic guardrails or an LLM-as-judge.

## Current Status

A minimal Z3 example has been implemented using a simplified employee leave eligibility policy.

## Setup

pip install -r requirements.txt

## Run

python toy_example.py

## Expected Output

Eligible result: unsat  
Not eligible result: sat  
Policy verdict: NOT ELIGIBLE
# Cross Validation

https://my.guild.ai/t/cross-validation/1017

## Problem

User is asking about making CV a single operation or using Guild to
generate one run per CV fold.

The recommended approach today is to implement cross validation as a
single Guild operation that trains on the various folds, generating a
final result. Conceptually, this treats the CV process as a single
training operation.

## Example of Guild-driven CV

The example in this project shows how Guild might be used to drive a
cross validation scenario. It's not a complete example as it relies on
an upcoming [*summary
operations*](https://my.guild.ai/t/summary-operations/872) feature.

See [`guild.yml`](guild.yml) for a way to break down data prep,
training, and summary into separate operations.

The `summary` operation is simulated to demonstrate how a summary
operation would be implemented.

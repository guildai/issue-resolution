# Support for filtering runs by date

https://github.com/guildai/guildai/issues/43

## Problem

There's no easy way to delete runs older than a particular date.

Related goals:

- Export runs from a particular day
- Label runs between two dates, or within some time frame

## Approach

Add a `--started` option to the list of runs filter options. The
`--started` option would accept one argument, which is a time range
spec. Time range specs can be expressed using a simple grammar,
described below.

## Time range spec grammar

```
spec : unit-range
     | operator-range
     | last-unit
     | explicit-range

unit-range : TODAY
           | YESTERDAY
           | THIS unit
           | NUMBER unit AGO

unit : MINUTE | HOUR | DAY | WEEK | MONTH | YEAR

operator-range : operator range

operator : BEFORE | AFTER

datetime : date | time | date time

date : SHORTDATE | MEDIUMDATE | LONGDATE

time : SHORTTIME | LONGTIME

last-unit : LAST delta-unit
          | LAST NUMBER delta-unit

delta-unit : MINUTE | HOUR | DAY

explicit-range : BETWEEN range AND range

range : unit-range | operator-range | datetime
```

### Examples

Implied range:

    today
    yesterday
    this week
    this month
    this year
    last week
    2 days ago
    1 week ago
    5 days ago
    5-12
    2018-5-12
    5-12 10:00

Explicit before:

    before today
    before this week
    before 5-12
    before 2019-5-12
    before 2018-12-1 1:00
    before 1 day ago

Explicit after:

    after yesterday
    after 2 days ago
    after 1 day ago
    after 5-12
    after 2018-5-12
    after 5-12 10:00

Explicit range:

    between 5-12 and now
    between 5-12 and 7-12
    between 7-12 and 5-12
    between 5 days ago and 2 days ago

## Implementation

Available in in 0.6.6.dev3

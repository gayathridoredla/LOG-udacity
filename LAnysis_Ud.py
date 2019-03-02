#!/usr/bin/env python
"Log-Analysis Project"
import psycopg2


def cct_dbse():
    """Connects to the news database and return a database cursor."""
    try:
        dtbse = psycopg2.connect("dbname=news")
        cors1 = dtbse.cursor()
    except Exception as error:
        print(error)
        return None
    else:
        return cors1


def mt_pp_te_aes(db1a_cors1):
    """Query and print out the 3 most popular articles.
    Args:
        db_cursor: psycopg2 PostgreSQL database cursor object.
    """
    qy_128 = """
            SELECT title, views FROM lanysis_ales INNER JOIN articles ON
    articles.slug = lanysis_ales.slug ORDER BY views desc LIMIT 3;
    """
    db1a_cors1.execute(qy_128)
    rsg_12 = db1a_cors1.fetchall()
    print(" a).Three Most Popular Articles Of All Time??")
    print(" ========================================")

    for rsg_12 in rsg_12:
        print(' --{title}  ------)  {count} views'
              .format(title=rsg_12[0], count=rsg_12[1]))
        print("\n")
    return


def m_ppar_ators(db1a_cors1):
    """Query and print out the most popular authors.
    Args:
        db_cursor: psycopg2 PostgreSQL database cursor object.
    """
    qe_23y = """
            SELECT laors_name.name AS author,
    sum(lanysis_ales.views) AS views FROM lanysis_ales INNER JOIN laors_name
    ON laors_name.slug=lanysis_ales.slug
    GROUP BY laors_name.name ORDER BY views desc limit 4;
    """
    db1a_cors1.execute(qe_23y)
    rsg_12 = db1a_cors1.fetchall()

    print(" b).Most Popular Authors Of All Time??")
    print(" =================================")

    for rsg_12 in rsg_12:
        print(' --{author}  ------)  {count} views'
              .format(author=rsg_12[0], count=rsg_12[1]))
        print("\n")
    return


def ds_ger_thn_eros(db1a_cors1):
    """Query and print out days where the error rate is greater than 1%.
    Args:
        db_cursor: psycopg2 PostgreSQL database cursor object.
    """
    qu_a1x = """
            SELECT leror_fail.date ,(
            leror_fail.count*100.00 / lanysis_total.count) AS
    percentage FROM leror_fail INNER JOIN lanysis_total
    ON leror_fail.date = lanysis_total.date
    AND (leror_fail.count*100.00 / lanysis_total.count) >1
    ORDER BY (leror_fail.count*100.00 /lanysis_total.count) desc;
    """
    db1a_cors1.execute(qu_a1x)
    rsg_12 = db1a_cors1.fetchall()

    print(" c).Days With Greater Than 1% Errors??")
    print(" =================================")

    for rsg_12 in rsg_12:
        print(' --{date:%B %d, %Y}  ------)  {error_rate:.1f}% errors'.format(
            date=rsg_12[0],
            error_rate=rsg_12[1]))
        print("\n")
        print(" **success** ")
    return


if __name__ == "__main__":
    CORS1 = cct_dbse()
    if CORS1:
        mt_pp_te_aes(CORS1)
        m_ppar_ators(CORS1)
        ds_ger_thn_eros(CORS1)
    CORS1.close()

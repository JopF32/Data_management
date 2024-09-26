query_1 = """
    WITH Calificaciones AS (
        SELECT 
            inscripciones.asignatura_id, 
            inscripciones.calificacion,
            estudiantes.nombre AS nombre_alumno,
            DENSE_RANK() OVER (PARTITION BY inscripciones.asignatura_id ORDER BY inscripciones.calificacion DESC) AS rank
        FROM 
            inscripciones
        JOIN 
            estudiantes ON estudiantes.numero_cuenta = inscripciones.num_cuenta
    ),
    Promedios AS (
        SELECT 
            asignatura_id,
            ROUND(AVG(CAST(calificacion AS FLOAT)), 2) AS calificacion_promedio 
        FROM 
            inscripciones
        GROUP BY 
            asignatura_id
    )
    SELECT 
        c.nombre_alumno,
        a.nombre AS nombre_materia, 
        c.calificacion,
        p.calificacion_promedio,
        CASE 
            WHEN c.calificacion > p.calificacion_promedio THEN 1 
            ELSE 0 
        END AS bandera1
    FROM 
        Calificaciones c
    JOIN 
        Promedios p ON c.asignatura_id = p.asignatura_id
    JOIN 
        asignaturas a ON c.asignatura_id = a.asignatura_id 
    WHERE 
        c.rank <= 3
    ORDER BY 
        c.asignatura_id, c.calificacion DESC;    
    """


query_2 = """
    WITH Materias AS (
        SELECT 
            DISTINCT(COUNT(asignatura_id)) AS total_materias
        FROM 
            asignaturas
    ),
    Avance AS (
        SELECT 
            estudiantes.nombre AS nombre_alumno,
            COUNT(inscripciones.calificacion) AS total_materias_cursadas,
            (SELECT total_materias FROM Materias) AS total_materias,
            COUNT(inscripciones.calificacion) * 100.0 / (SELECT total_materias FROM Materias) AS porcentaje_avance,
            CASE 
                WHEN COUNT(inscripciones.calificacion) = (SELECT total_materias FROM Materias) THEN 5
                WHEN COUNT(inscripciones.calificacion) >= (0.8 * (SELECT total_materias FROM Materias)) THEN 4
                WHEN COUNT(inscripciones.calificacion) >= (0.65 * (SELECT total_materias FROM Materias)) THEN 3
                WHEN COUNT(inscripciones.calificacion) >= (0.4 * (SELECT total_materias FROM Materias)) THEN 2
                ELSE 1
            END AS bandera_calificacion
        FROM 
            inscripciones
        JOIN 
            estudiantes ON estudiantes.numero_cuenta = inscripciones.num_cuenta
        WHERE 
            inscripciones.calificacion IS NOT NULL  
        GROUP BY 
            estudiantes.nombre
    )
    SELECT 
        nombre_alumno,
        total_materias_cursadas,
        total_materias,
        FORMAT(ROUND(porcentaje_avance, 2), 'N2') AS porcentaje_avance,
        bandera_calificacion
    FROM 
        Avance
    ORDER BY 
        porcentaje_avance DESC;
        """
        
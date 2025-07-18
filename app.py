import random

from flask import Flask, render_template

app = Flask(__name__)


cursos = [
    {
        'id': 1,
        'titulo': 'Curso Completo de Desarrollo Web: HTML, CSS, JavaScript y Frameworks',
        'categoria': 'Desarrollo',
        'descripcion': 'Aprende a crear sitios web modernos, responsivos y profesionales desde cero hasta avanzado.',
        'imagen': 'web.jpg',
        'estrellas': 4.7,
        'precio': 130,
        'duracion': '45 horas',
        'estudiantes': 25430,
        'ultima_actualizacion': '07/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado de finalización, proyectos prácticos, asistencia personalizada',
        'lo_que_aprenderas': [
            'Crear páginas web responsivas con HTML5 y CSS3 modernos.',
            'Programar con JavaScript y manipular el DOM.',
            'Usar frameworks populares como React y Vue.js.',
            'Diseñar interfaces atractivas y accesibles.',
            'Optimizar sitios para SEO y rendimiento.',
            'Desarrollar proyectos reales para tu portafolio profesional.'
        ],
        'requisitos': [
            'No se requiere experiencia previa en programación.',
            'Ganas de aprender y practicar.',
            'Computadora con acceso a internet.'
        ],
        'contenido_curso': {
            'secciones': 12,
            'clases': 78,
            'duracion_total': '45 horas',
            'detalle': [
                'Introducción al desarrollo web y configuración del entorno.',
                'HTML5 básico y avanzado.',
                'CSS3 y diseño responsivo.',
                'JavaScript moderno ES6+.',
                'Manipulación del DOM y eventos.',
                'Introducción a frameworks: React y Vue.js.',
                'Optimización SEO y buenas prácticas.',
                'Proyecto final: crear un sitio web completo.'
            ]
        }
    },
    {
        'id': 2,
        'titulo': 'Curso Completo de Arquitectura Moderna y Diseño Innovador',
        'categoria': 'Arquitectura',
        'descripcion': 'Domina el diseño de planos y estructuras con técnicas modernas y software especializado.',
        'imagen': 'arquitectura.jpg',
        'estrellas': 4.5,
        'precio': 120,
        'duracion': '38 horas',
        'estudiantes': 15300,
        'ultima_actualizacion': '06/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado profesional, recursos descargables, asistencia personalizada',
        'lo_que_aprenderas': [
            'Interpretar y diseñar planos arquitectónicos modernos.',
            'Usar software CAD y BIM para modelado 3D.',
            'Conceptos de sostenibilidad y diseño ecológico.',
            'Aplicar normas técnicas y regulaciones actuales.',
            'Gestionar proyectos de arquitectura con éxito.',
            'Presentar propuestas efectivas a clientes.'
        ],
        'requisitos': [
            'Conocimientos básicos de dibujo técnico.',
            'Interés en diseño y construcción.',
            'Computadora con software recomendado.'
        ],
        'contenido_curso': {
            'secciones': 10,
            'clases': 60,
            'duracion_total': '38 horas',
            'detalle': [
                'Fundamentos de arquitectura y diseño contemporáneo.',
                'Introducción a software CAD y BIM.',
                'Diseño ecológico y sostenible.',
                'Normativas y regulaciones.',
                'Proyectos y casos prácticos.'
            ]
        }
    },
    {
        'id': 3,
        'titulo': 'Curso de Administración de Empresas: Gestión y Estrategias Efectivas',
        'categoria': 'Administración',
        'descripcion': 'Aprende a dirigir y gestionar negocios exitosos con estrategias modernas y herramientas prácticas.',
        'imagen': 'admin.jpg',
        'estrellas': 4.8,
        'precio': 110,
        'duracion': '40 horas',
        'estudiantes': 18900,
        'ultima_actualizacion': '07/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado oficial, casos reales, asistencia de expertos',
        'lo_que_aprenderas': [
            'Planificación estratégica y gestión operativa.',
            'Liderazgo y desarrollo de equipos.',
            'Manejo financiero y control de costos.',
            'Marketing y ventas para empresas.',
            'Toma de decisiones basada en datos.',
            'Gestión de proyectos y mejora continua.'
        ],
        'requisitos': [
            'Interés en gestión empresarial.',
            'Conocimientos básicos de administración.',
            'Computadora con acceso a internet.'
        ],
        'contenido_curso': {
            'secciones': 11,
            'clases': 65,
            'duracion_total': '40 horas',
            'detalle': [
                'Introducción a la administración moderna.',
                'Gestión financiera y presupuestos.',
                'Marketing y ventas estratégicas.',
                'Liderazgo y desarrollo humano.',
                'Casos prácticos y simulaciones.'
            ]
        }
    },
    {
        'id': 4,
        'titulo': 'Curso Profesional de Marketing Digital y Redes Sociales',
        'categoria': 'Marketing',
        'descripcion': 'Domina las estrategias digitales para posicionar productos y marcas en el entorno online.',
        'imagen': 'marketing.jpg',
        'estrellas': 4.6,
        'precio': 100,
        'duracion': '35 horas',
        'estudiantes': 21000,
        'ultima_actualizacion': '05/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado, acceso a herramientas, asesoría personalizada',
        'lo_que_aprenderas': [
            'Planificar campañas en Google Ads y Facebook Ads.',
            'SEO para mejorar el posicionamiento web.',
            'Gestión de redes sociales y contenido viral.',
            'Email marketing y automatización.',
            'Análisis de métricas y optimización de resultados.',
            'Creación de funnels y embudos de venta efectivos.'
        ],
        'requisitos': [
            'Interés en marketing y ventas.',
            'Nociones básicas de internet.',
            'Computadora y conexión a internet.'
        ],
        'contenido_curso': {
            'secciones': 9,
            'clases': 50,
            'duracion_total': '35 horas',
            'detalle': [
                'Fundamentos de marketing digital.',
                'Publicidad en redes sociales.',
                'SEO y posicionamiento web.',
                'Email marketing y funnels de venta.',
                'Análisis y métricas digitales.'
            ]
        }
    },
    {
        'id': 5,
        'titulo': 'Curso de Fotografía Profesional: Técnicas y Edición',
        'categoria': 'Fotografía',
        'descripcion': 'Aprende a capturar y editar fotografías profesionales con técnicas avanzadas y software especializado.',
        'imagen': 'fotografia.jpg',
        'estrellas': 4.7,
        'precio': 115,
        'duracion': '30 horas',
        'estudiantes': 17500,
        'ultima_actualizacion': '06/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado, acceso a recursos, ejercicios prácticos',
        'lo_que_aprenderas': [
            'Manejo de cámaras DSLR y sin espejo.',
            'Composición y encuadre fotográfico.',
            'Iluminación natural y artificial.',
            'Edición avanzada con Photoshop y Lightroom.',
            'Creación de portafolio profesional.',
            'Técnicas para fotografía de retrato y paisaje.'
        ],
        'requisitos': [
            'Cámara digital o smartphone avanzado.',
            'Ganas de aprender y practicar.',
            'Computadora para edición fotográfica.'
        ],
        'contenido_curso': {
            'secciones': 8,
            'clases': 45,
            'duracion_total': '30 horas',
            'detalle': [
                'Fundamentos de fotografía.',
                'Técnicas de iluminación.',
                'Edición digital.',
                'Proyectos fotográficos.'
            ]
        }
    },
    {
        'id': 6,
        'titulo': 'Curso Básico de Python para Principiantes',
        'categoria': 'Desarrollo',
        'descripcion': 'Introducción completa a la programación con Python, ideal para quienes nunca programaron.',
        'imagen': 'python.jpg',
        'estrellas': 4.9,
        'precio': 90,
        'duracion': '25 horas',
        'estudiantes': 32000,
        'ultima_actualizacion': '07/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado, ejercicios prácticos, soporte docente',
        'lo_que_aprenderas': [
            'Conceptos básicos de programación y lógica.',
            'Sintaxis y estructuras de Python.',
            'Manejo de variables, listas y diccionarios.',
            'Introducción a funciones y módulos.',
            'Desarrollo de proyectos simples.',
            'Buenas prácticas en programación.'
        ],
        'requisitos': [
            'Ganas de aprender a programar.',
            'Computadora con Python instalado.',
            'Acceso a internet para recursos.'
        ],
        'contenido_curso': {
            'secciones': 7,
            'clases': 40,
            'duracion_total': '25 horas',
            'detalle': [
                'Introducción a Python.',
                'Tipos de datos y variables.',
                'Estructuras de control.',
                'Funciones y módulos.',
                'Proyecto final básico.'
            ]
        }
    },
    {
        'id': 7,
        'titulo': 'Curso de Diseño Gráfico para Principiantes y Profesionales',
        'categoria': 'Diseño',
        'descripcion': 'Aprende a crear imágenes, logos y material gráfico con las herramientas más populares.',
        'imagen': 'diseno.jpg',
        'estrellas': 4.5,
        'precio': 95,
        'duracion': '28 horas',
        'estudiantes': 14200,
        'ultima_actualizacion': '05/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado, acceso a recursos gráficos, tutorías',
        'lo_que_aprenderas': [
            'Fundamentos del diseño gráfico.',
            'Uso de Adobe Photoshop y Canva.',
            'Creación de logos y branding.',
            'Diseño para redes sociales y web.',
            'Técnicas de edición y retoque.',
            'Presentación de proyectos gráficos.'
        ],
        'requisitos': [
            'Ganas de aprender diseño gráfico.',
            'Computadora con software necesario.',
            'Creatividad y paciencia.'
        ],
        'contenido_curso': {
            'secciones': 7,
            'clases': 42,
            'duracion_total': '28 horas',
            'detalle': [
                'Fundamentos del diseño.',
                'Herramientas digitales.',
                'Proyectos y ejercicios prácticos.'
            ]
        }
    },
    {
        'id': 8,
        'titulo': 'Curso de Finanzas Personales: Administración y Ahorro',
        'categoria': 'Finanzas',
        'descripcion': 'Aprende a administrar tu dinero, ahorrar y planificar para un futuro financiero seguro.',
        'imagen': 'finanzas.jpg',
        'estrellas': 4.4,
        'precio': 80,
        'duracion': '22 horas',
        'estudiantes': 16500,
        'ultima_actualizacion': '06/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado, hojas de trabajo, asesoría financiera',
        'lo_que_aprenderas': [
            'Conceptos básicos de finanzas personales.',
            'Elaborar presupuestos efectivos.',
            'Técnicas para ahorro inteligente.',
            'Uso responsable del crédito y deudas.',
            'Planificación financiera a corto y largo plazo.',
            'Inversiones básicas y seguridad financiera.'
        ],
        'requisitos': [
            'Interés en mejorar tus finanzas.',
            'Computadora o smartphone.',
            'Ganas de aprender y aplicar.'
        ],
        'contenido_curso': {
            'secciones': 6,
            'clases': 30,
            'duracion_total': '22 horas',
            'detalle': [
                'Introducción a las finanzas personales.',
                'Presupuestos y ahorro.',
                'Planificación y estrategias.'
            ]
        }
    },
    
    {
        'id': 9,
        'titulo': 'Curso de Cocina Internacional: Técnicas y Recetas Globales',
        'categoria': 'Gastronomía',
        'descripcion': 'Descubre y domina recetas de diversas culturas y técnicas culinarias profesionales.',
        'imagen': 'cocina.jpg',
        'estrellas': 4.7,
        'precio': 105,
        'duracion': '33 horas',
        'estudiantes': 12700,
        'ultima_actualizacion': '07/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado, recetas descargables, soporte culinario',
        'lo_que_aprenderas': [
            'Técnicas básicas y avanzadas de cocina.',
            'Recetas tradicionales de diferentes países.',
            'Preparación y presentación profesional.',
            'Higiene y seguridad alimentaria.',
            'Planificación de menús variados.',
            'Consejos para emprender en gastronomía.'
        ],
        'requisitos': [
            'Interés en la cocina.',
            'Acceso a cocina equipada.',
            'Ganas de aprender y practicar.'
        ],
        'contenido_curso': {
            'secciones': 8,
            'clases': 48,
            'duracion_total': '33 horas',
            'detalle': [
                'Introducción a la cocina internacional.',
                'Técnicas culinarias.',
                'Recetas y preparación.',
                'Proyectos culinarios.'
            ]
        }
    },
    {
        'id': 10,
        'titulo': 'Curso Avanzado de Inteligencia Artificial y Aprendizaje Automático',
        'categoria': 'Tecnología',
        'descripcion': 'Explora los fundamentos y aplicaciones prácticas de la inteligencia artificial y machine learning.',
        'imagen': 'ia.jpg',
        'estrellas': 4.6,
        'precio': 140,
        'duracion': '50 horas',
        'estudiantes': 9000,
        'ultima_actualizacion': '07/2025',
        'idioma': 'Español',
        'acceso': 'Acceso de por vida en dispositivos móviles y TV',
        'beneficios': 'Certificado, proyectos reales, soporte experto',
        'lo_que_aprenderas': [
            'Fundamentos de IA y machine learning.',
            'Técnicas de procesamiento de datos.',
            'Modelos supervisados y no supervisados.',
            'Redes neuronales y deep learning.',
            'Aplicaciones prácticas en diferentes industrias.',
            'Uso de herramientas y librerías Python.'
        ],
        'requisitos': [
            'Conocimientos básicos de programación.',
            'Matemáticas básicas (álgebra, estadística).',
            'Interés en tecnología y datos.'
        ],
        'contenido_curso': {
            'secciones': 14,
            'clases': 85,
            'duracion_total': '50 horas',
            'detalle': [
                'Introducción a IA y machine learning.',
                'Preparación y limpieza de datos.',
                'Modelos supervisados.',
                'Redes neuronales.',
                'Proyectos y casos prácticos.'
            ]
        }
    },
    {
    'id': 11,
    'titulo': 'Curso de Programación con Java',
    'categoria': 'Desarrollo',
    'descripcion': 'Aprende sobre programación con java con un curso completo y actualizado.',
    'imagen': 'desarrollo.jpg',
    'estrellas': 4.8,
    'precio': 74,
    'duracion': '18 horas',
    'estudiantes': 13450,
    'ultima_actualizacion': '04/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado de finalización, Ejercicios prácticos, Acceso de por vida',
    'lo_que_aprenderas': [
        'Conceptos básicos de programación con java.',
        'Aplicación práctica de programación con java.',
        'Herramientas y recursos útiles.',
        'Proyectos para fortalecer el aprendizaje.',
        'Buenas prácticas y consejos profesionales.'
    ],
    'requisitos': [
        'Ganas de aprender.',
        'Computadora o dispositivo con acceso a internet.',
        'Conocimientos básicos relacionados (según curso).'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 17,
        'duracion_total': '18 horas',
        'detalle': [
            'Introducción y fundamentos.',
            'Temas principales y técnicas.',
            'Prácticas y ejercicios.',
            'Proyecto final o casos de estudio.',
            'Resumen y conclusiones.'
        ]
    }
},
{
    'id': 12,
    'titulo': 'Curso de Diseño de Interiores Modernos',
    'categoria': 'Arquitectura',
    'descripcion': 'Aprende sobre diseño de interiores modernos con un curso completo y actualizado.',
    'imagen': 'interior.jpg',
    'estrellas': 4.5,
    'precio': 68,
    'duracion': '20 horas',
    'estudiantes': 10230,
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Material descargable, Certificado de finalización, Tutorías especializadas',
    'lo_que_aprenderas': [
        'Conceptos básicos de diseño de interiores modernos.',
        'Aplicación práctica de diseño de interiores modernos.',
        'Herramientas y recursos útiles.',
        'Proyectos para fortalecer el aprendizaje.',
        'Buenas prácticas y consejos profesionales.'
    ],
    'requisitos': [
        'Ganas de aprender.',
        'Computadora o dispositivo con acceso a internet.',
        'Conocimientos básicos relacionados (según curso).'
    ],
    'contenido_curso': {
        'secciones': 4,
        'clases': 16,
        'duracion_total': '20 horas',
        'detalle': [
            'Introducción y fundamentos.',
            'Temas principales y técnicas.',
            'Prácticas y ejercicios.',
            'Proyecto final o casos de estudio.',
            'Resumen y conclusiones.'
        ]
    }
},
{
    'id': 13,
    'titulo': 'Curso de Gestión de Recursos Humanos',
    'categoria': 'Administración',
    'descripcion': 'Aprende sobre gestión de recursos humanos con un curso completo y actualizado.',
    'imagen': 'administracion.jpg',
    'estrellas': 4.7,
    'precio': 80,
    'duracion': '19 horas',
    'estudiantes': 18500,
    'ultima_actualizacion': '03/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado oficial, Acceso de por vida, Proyectos reales',
    'lo_que_aprenderas': [
        'Conceptos básicos de gestión de recursos humanos.',
        'Aplicación práctica de gestión de recursos humanos.',
        'Herramientas y recursos útiles.',
        'Proyectos para fortalecer el aprendizaje.',
        'Buenas prácticas y consejos profesionales.'
    ],
    'requisitos': [
        'Ganas de aprender.',
        'Computadora o dispositivo con acceso a internet.',
        'Conocimientos básicos relacionados (según curso).'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '19 horas',
        'detalle': [
            'Introducción y fundamentos.',
            'Temas principales y técnicas.',
            'Prácticas y ejercicios.',
            'Proyecto final o casos de estudio.',
            'Resumen y conclusiones.'
        ]
    }
},
{
    'id': 14,
    'titulo': 'Curso de Marketing de Contenidos',
    'categoria': 'Marketing',
    'descripcion': 'Aprende sobre marketing de contenidos con un curso completo y actualizado.',
    'imagen': 'contenido.jpg',
    'estrellas': 4.6,
    'precio': 70,
    'duracion': '17 horas',
    'estudiantes': 17650,
    'ultima_actualizacion': '05/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, Material descargable, Tutorías especializadas',
    'lo_que_aprenderas': [
        'Conceptos básicos de marketing de contenidos.',
        'Aplicación práctica de marketing de contenidos.',
        'Herramientas y recursos útiles.',
        'Proyectos para fortalecer el aprendizaje.',
        'Buenas prácticas y consejos profesionales.'
    ],
    'requisitos': [
        'Ganas de aprender.',
        'Computadora o dispositivo con acceso a internet.',
        'Conocimientos básicos relacionados (según curso).'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 18,
        'duracion_total': '17 horas',
        'detalle': [
            'Introducción y fundamentos.',
            'Temas principales y técnicas.',
            'Prácticas y ejercicios.',
            'Proyecto final o casos de estudio.',
            'Resumen y conclusiones.'
        ]
    }
},
{
    'id': 15,
    'titulo': 'Curso Básico de Electricidad para el Hogar',
    'categoria': 'Tecnología',
    'descripcion': 'Aprende los fundamentos de la electricidad para hacer mantenimientos básicos en casa.',
    'imagen': 'electricidad.jpg',
    'estrellas': 4.4,
    'precio': 50,
    'duracion': '17 horas',
    'estudiantes': 7400,
    'ultima_actualizacion': '04/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, Acceso de por vida, Manual descargable',
    'lo_que_aprenderas': [
        'Conceptos básicos de electricidad.',
        'Seguridad y precauciones.',
        'Instalaciones y mantenimientos simples.',
        'Herramientas necesarias.',
        'Diagnóstico de fallas comunes.'
    ],
    'requisitos': [
        'Ganas de aprender y practicar.',
        'Herramientas básicas (según curso).',
        'Interés en mantenimiento doméstico.'
    ],
    'contenido_curso': {
        'secciones': 4,
        'clases': 14,
        'duracion_total': '17 horas',
        'detalle': [
            'Fundamentos y seguridad.',
            'Herramientas y materiales.',
            'Mantenimientos básicos.',
            'Proyectos prácticos.'
        ]
    }
},
{
    'id': 16,
    'titulo': 'Curso de Finanzas para Emprendedores',
    'categoria': 'Finanzas',
    'descripcion': 'Aprende a manejar las finanzas de tu negocio para crecer de forma rentable y sostenible.',
    'imagen': 'finanzasemp.jpg',
    'estrellas': 4.6,
    'precio': 78,
    'duracion': '19 horas',
    'estudiantes': 9800,
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Casos reales, Certificado, Asesoría financiera',
    'lo_que_aprenderas': [
        'Gestión financiera básica para negocios.',
        'Elaboración de presupuestos y flujos.',
        'Manejo de costos y precios.',
        'Análisis de rentabilidad.',
        'Planificación financiera estratégica.'
    ],
    'requisitos': [
        'Interés en negocios y finanzas.',
        'Computadora o smartphone.',
        'Ganas de aprender y aplicar.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '19 horas',
        'detalle': [
            'Introducción a finanzas para emprendedores.',
            'Presupuestos y flujos de caja.',
            'Costos y precios.',
            'Análisis financiero.',
            'Planificación y estrategia.'
        ]
    }
},
{
    'id': 17,
    'titulo': 'Curso Práctico de Reparación de Computadoras',
    'categoria': 'Tecnología',
    'descripcion': 'Aprende a diagnosticar y reparar problemas comunes en computadoras de escritorio y laptops.',
    'imagen': 'reparacion_pc.jpg',
    'estrellas': 4.4,
    'precio': 72,
    'duracion': '19 horas',
    'estudiantes': 8200,
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, videos paso a paso, soporte experto',
    'lo_que_aprenderas': [
        'Diagnóstico de hardware y software.',
        'Reparación y mantenimiento básico.',
        'Instalación de sistemas operativos.',
        'Optimización del rendimiento.',
        'Prevención de fallos comunes.'
    ],
    'requisitos': [
        'Interés en tecnología y computadoras.',
        'Ganas de aprender y practicar.',
        'Herramientas básicas recomendadas.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 18,
        'duracion_total': '19 horas',
        'detalle': [
            'Introducción y seguridad.',
            'Diagnóstico de problemas.',
            'Reparación básica.',
            'Instalación y mantenimiento.',
            'Consejos y proyectos prácticos.'
        ]
    }
},
{
    'id': 18,
    'titulo': 'Curso Básico de Ilustración Digital',
    'categoria': 'Diseño',
    'descripcion': 'Aprende las técnicas fundamentales para crear ilustraciones digitales usando software popular.',
    'imagen': 'ilustracion_digital.jpg',
    'estrellas': 4.5,
    'precio': 70,
    'duracion': '19 horas',
    'estudiantes': 9700,
    'ultima_actualizacion': '05/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, ejercicios prácticos, recursos descargables',
    'lo_que_aprenderas': [
        'Herramientas básicas de ilustración digital.',
        'Técnicas de dibujo y color.',
        'Uso de tabletas y software como Photoshop.',
        'Creación de personajes y fondos.',
        'Preparación de archivos para impresión y web.'
    ],
    'requisitos': [
        'Computadora o tableta gráfica.',
        'Ganas de aprender y practicar.',
        'Interés en diseño e ilustración.'
    ],
     'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '19 horas',
        'detalle': [
            'Introducción a la ilustración digital.',
            'Herramientas y técnicas básicas.',
            'Dibujo y color.',
            'Proyectos prácticos.',
            'Exportación y publicación.'
        ]
    }
},
{
    'id': 19,
    'titulo': 'Curso Básico de Ofimática: Word, Excel y PowerPoint',
    'categoria': 'Ofimática',
    'descripcion': 'Domina las herramientas básicas de ofimática para mejorar tu productividad en el trabajo y estudio.',
    'imagen': 'ofimatica.jpg',
    'estrellas': round(random.uniform(4.3, 4.8), 1),
    'precio': random.randint(50, 130),
    'duracion': '18 horas',
    'estudiantes': random.randint(8000, 20000),
    'ultima_actualizacion': '06/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado oficial, ejercicios prácticos, soporte docente',
    'lo_que_aprenderas': [
        'Uso básico y avanzado de Microsoft Word.',
        'Introducción a Microsoft Excel.',
        'Creación de presentaciones profesionales con PowerPoint.',
        'Manejo de plantillas y formatos.',
        'Consejos para mejorar la productividad con ofimática.'
    ],
    'requisitos': [
        'Nociones básicas de informática.',
        'Computadora con Microsoft Office instalado.',
        'Ganas de aprender y practicar.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '18 horas',
        'detalle': [
            'Introducción a Microsoft Word.',
            'Formato y edición de documentos.',
            'Introducción a Excel básico.',
            'Creación de presentaciones en PowerPoint.',
            'Consejos y trucos para productividad.'
        ]
    }
},
{
    'id': 20,
    'titulo': 'Curso Avanzado de Excel: Funciones, Tablas Dinámicas y Macros',
    'categoria': 'Ofimática',
    'descripcion': 'Aprende técnicas avanzadas para dominar Excel, desde funciones complejas hasta automatización con macros.',
    'imagen': 'excel_avanzado.jpg',
    'estrellas': round(random.uniform(4.5, 5.0), 1),
    'precio': random.randint(70, 130),
    'duracion': '20 horas',
    'estudiantes': random.randint(7000, 18000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado profesional, ejercicios prácticos, soporte especializado',
    'lo_que_aprenderas': [
        'Uso avanzado de funciones y fórmulas en Excel.',
        'Creación y análisis con tablas dinámicas.',
        'Automatización de tareas con Macros y VBA.',
        'Optimización de hojas de cálculo para proyectos reales.',
        'Visualización de datos con gráficos avanzados.'
    ],
    'requisitos': [
        'Conocimientos básicos de Excel.',
        'Computadora con Microsoft Excel instalado.',
        'Interés en automatización y análisis de datos.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 18,
        'duracion_total': '20 horas',
        'detalle': [
            'Funciones avanzadas y fórmulas personalizadas.',
            'Tablas dinámicas y segmentación de datos.',
            'Introducción a Macros y VBA.',
            'Optimización y auditoría de hojas.',
            'Proyectos prácticos con casos reales.'
        ]
    }
},
{
    'id': 21,
    'titulo': 'Curso de Inglés Básico para Principiantes',
    'categoria': 'Idiomas',
    'descripcion': 'Inicia tu aprendizaje en inglés con fundamentos sólidos para comunicarte en situaciones cotidianas.',
    'imagen': 'ingles_basico.jpg',
    'estrellas': round(random.uniform(4.3, 4.8), 1),
    'precio': random.randint(50, 100),
    'duracion': '20 horas',
    'estudiantes': random.randint(10000, 25000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, ejercicios prácticos, tutorías personalizadas',
    'lo_que_aprenderas': [
        'Vocabulario básico y expresiones comunes.',
        'Gramática esencial para conversaciones simples.',
        'Práctica de comprensión auditiva y pronunciación.',
        'Escritura y lectura básica en inglés.',
        'Estrategias para continuar aprendiendo.'
    ],
    'requisitos': [
        'Ningún conocimiento previo en inglés.',
        'Ganas de aprender y practicar.',
        'Acceso a internet y dispositivo para clases.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 18,
        'duracion_total': '20 horas',
        'detalle': [
            'Introducción al inglés básico.',
            'Vocabulario y frases comunes.',
            'Gramática esencial.',
            'Prácticas de conversación.',
            'Lectura y escritura básicas.'
        ]
    }
},
{
    'id': 22,
    'titulo': 'Curso Avanzado de Excel para Análisis de Datos',
    'categoria': 'Ofimática',
    'descripcion': 'Domina funciones avanzadas, tablas dinámicas y macros para análisis efectivo de datos.',
    'imagen': 'excel_analisis.jpg',
    'estrellas': round(random.uniform(4.5, 4.9), 1),
    'precio': random.randint(50, 130),
    'duracion': '18 horas',
    'estudiantes': random.randint(10000, 22000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, ejercicios prácticos, soporte docente',
    'lo_que_aprenderas': [
        'Funciones avanzadas de Excel.',
        'Creación y manejo de tablas dinámicas.',
        'Automatización con macros.',
        'Visualización de datos con gráficos.',
        'Análisis y manejo de grandes volúmenes de datos.'
    ],
    'requisitos': [
        'Conocimientos básicos de Excel.',
        'Computadora con Microsoft Excel instalado.',
        'Ganas de mejorar habilidades.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '18 horas',
        'detalle': [
            'Funciones avanzadas y fórmulas.',
            'Tablas dinámicas y gráficos.',
            'Introducción a macros.',
            'Automatización y VBA básica.',
            'Proyecto final de análisis de datos.'
        ]
    }
},
{
    'id': 23,
    'titulo': 'Curso de Cocina Saludable y Nutrición Básica',
    'categoria': 'Gastronomía',
    'descripcion': 'Aprende a preparar comidas saludables con recetas nutritivas y técnicas de cocina fácil.',
    'imagen': 'cocina_saludable.jpg',
    'estrellas': round(random.uniform(4.4, 4.7), 1),
    'precio': random.randint(50, 130),
    'duracion': '14 horas',
    'estudiantes': random.randint(7000, 14000),
    'ultima_actualizacion': '06/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, recetas descargables, consejos nutricionales',
    'lo_que_aprenderas': [
        'Principios básicos de nutrición.',
        'Planificación de comidas saludables.',
        'Técnicas de cocina baja en grasas y azúcares.',
        'Preparación de recetas nutritivas y sabrosas.',
        'Consejos para mantener una dieta equilibrada.'
    ],
    'requisitos': [
        'Interés en alimentación saludable.',
        'Acceso a cocina básica.',
        'Ganas de aprender y mejorar hábitos.'
    ],
    'contenido_curso': {
        'secciones': 3,
        'clases': 14,
        'duracion_total': '14 horas',
        'detalle': [
            'Introducción a la nutrición.',
            'Recetas saludables.',
            'Consejos y plan de alimentación.'
        ]
    }
},
{
    'id': 24,
    'titulo': 'Curso de Diseño UX/UI para Principiantes',
    'categoria': 'Diseño',
    'descripcion': 'Aprende a diseñar experiencias de usuario intuitivas y atractivas para aplicaciones y sitios web.',
    'imagen': 'ux_ui.jpg',
    'estrellas': round(random.uniform(4.3, 4.7), 1),
    'precio': random.randint(50, 130),
    'duracion': '19 horas',
    'estudiantes': random.randint(10000, 20000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, proyectos prácticos, tutorías',
    'lo_que_aprenderas': [
        'Principios básicos de UX/UI.',
        'Herramientas de diseño digital.',
        'Creación de wireframes y prototipos.',
        'Testeo y optimización de interfaces.',
        'Tendencias actuales en diseño digital.'
    ],
    'requisitos': [
        'Interés en diseño digital.',
        'Computadora con software básico de diseño.',
        'Creatividad y ganas de aprender.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '19 horas',
        'detalle': [
            'Introducción a UX/UI.',
            'Herramientas y wireframes.',
            'Diseño visual y prototipos.',
            'Testeo y feedback.',
            'Proyecto final.'
        ]
    }
},
{
    'id': 25,
    'titulo': 'Curso Básico de Inglés Conversacional',
    'categoria': 'Idiomas',
    'descripcion': 'Desarrolla habilidades para comunicarte en inglés en situaciones cotidianas y profesionales.',
    'imagen': 'ingles.jpg',
    'estrellas': round(random.uniform(4.2, 4.6), 1),
    'precio': random.randint(50, 130),
    'duracion': '20 horas',
    'estudiantes': random.randint(12000, 22000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español e Inglés',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, audios y prácticas, tutorías online',
    'lo_que_aprenderas': [
        'Saludo y presentaciones.',
        'Conversación básica y frases comunes.',
        'Gramática esencial para comunicación.',
        'Comprensión auditiva.',
        'Expresiones para situaciones laborales.'
    ],
    'requisitos': [
        'Ningún conocimiento previo.',
        'Disposición para practicar regularmente.',
        'Acceso a internet para audios y videos.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '20 horas',
        'detalle': [
            'Saludos y presentaciones.',
            'Gramática básica.',
            'Conversación cotidiana.',
            'Audición y pronunciación.',
            'Prácticas y evaluación.'
        ]
    }
},
{
    'id': 26,
    'titulo': 'Curso Básico de Electricidad y Electrónica',
    'categoria': 'Tecnología',
    'descripcion': 'Conoce los fundamentos de electricidad y electrónica para proyectos básicos y reparaciones.',
    'imagen': 'electricidades.jpg',
    'estrellas': round(random.uniform(4.3, 4.7), 1),
    'precio': random.randint(50, 130),
    'duracion': '19 horas',
    'estudiantes': random.randint(7000, 13000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, prácticas y proyectos, soporte docente',
    'lo_que_aprenderas': [
        'Conceptos básicos de electricidad.',
        'Circuitos eléctricos simples.',
        'Componentes electrónicos comunes.',
        'Medición y seguridad eléctrica.',
        'Proyectos básicos de electrónica.'
    ],
    'requisitos': [
        'Interés en tecnología y electrónica.',
        'Ganas de aprender y practicar.',
        'Acceso a herramientas básicas.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 18,
        'duracion_total': '19 horas',
        'detalle': [
            'Fundamentos de electricidad.',
            'Circuitos y componentes.',
            'Medición y seguridad.',
            'Proyectos prácticos.',
            'Mantenimiento básico.'
        ]
    }
},
{
    'id': 27,
    'titulo': 'Curso de Primeros Auxilios y Seguridad Básica',
    'categoria': 'Salud',
    'descripcion': 'Aprende a actuar correctamente en emergencias con técnicas básicas de primeros auxilios.',
    'imagen': 'primeros_auxilios.jpg',
    'estrellas': round(random.uniform(4.5, 4.9), 1),
    'precio': random.randint(50, 130),
    'duracion': '17 horas',
    'estudiantes': random.randint(9000, 15000),
    'ultima_actualizacion': '06/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, simulacros, guía práctica',
    'lo_que_aprenderas': [
        'Evaluación de emergencias.',
        'RCP y maniobras básicas.',
        'Atención a heridas y fracturas.',
        'Prevención de accidentes.',
        'Planificación de seguridad familiar.'
    ],
    'requisitos': [
        'Interés en salud y seguridad.',
        'Ganas de aprender y ayudar.',
        'Acceso a materiales prácticos.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 18,
        'duracion_total': '17 horas',
        'detalle': [
            'Introducción a primeros auxilios.',
            'Técnicas de RCP.',
            'Atención de heridas.',
            'Prevención y seguridad.',
            'Simulacros y prácticas.'
        ]
    }
},
{
    'id': 28,
    'titulo': 'Curso de Creación y Edición de Videos para Redes Sociales',
    'categoria': 'Multimedia',
    'descripcion': 'Aprende a crear videos atractivos para redes sociales usando herramientas accesibles.',
    'imagen': 'edicion_video.jpg',
    'estrellas': round(random.uniform(4.4, 4.8), 1),
    'precio': random.randint(50, 130),
    'duracion': '19 horas',
    'estudiantes': random.randint(8000, 16000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, plantillas, ejercicios prácticos',
    'lo_que_aprenderas': [
        'Conceptos básicos de edición de video.',
        'Uso de software accesible (e.g. DaVinci Resolve, iMovie).',
        'Creación de contenido para redes sociales.',
        'Técnicas de animación y efectos.',
        'Exportación y publicación.'
    ],
    'requisitos': [
        'Computadora con capacidad básica de edición.',
        'Ganas de crear contenido audiovisual.',
        'Acceso a software recomendado.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '19 horas',
        'detalle': [
            'Introducción a edición de video.',
            'Herramientas básicas.',
            'Técnicas y efectos.',
            'Creación de contenido.',
            'Proyecto final.'
        ]
    }
},
{
    'id': 29,
    'titulo': 'Curso Básico de Pintura Acrílica para Principiantes',
    'categoria': 'Arte',
    'descripcion': 'Descubre las técnicas básicas para pintar con acrílicos y expresar tu creatividad.',
    'imagen': 'pintura_acrilica.jpg',
    'estrellas': round(random.uniform(4.4, 4.8), 1),
    'precio': random.randint(50, 130),
    'duracion': '14 horas',
    'estudiantes': random.randint(4000, 9000),
    'ultima_actualizacion': '05/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, materiales recomendados, ejercicios prácticos',
    'lo_que_aprenderas': [
        'Materiales y preparación del espacio.',
        'Técnicas básicas de pintura acrílica.',
        'Uso de colores y mezclas.',
        'Creación de composiciones simples.',
        'Cuidados y conservación de pinturas.'
    ],
    'requisitos': [
        'Ganas de pintar y crear.',
        'Materiales básicos de pintura acrílica.',
        'Espacio para trabajar.'
    ],
    'contenido_curso': {
        'secciones': 3,
        'clases': 14,
        'duracion_total': '14 horas',
        'detalle': [
            'Introducción y materiales.',
            'Técnicas básicas.',
            'Proyecto final.'
        ]
    }
},
{
    'id': 30,
    'titulo': 'Curso de Marketing para Negocios Locales',
    'categoria': 'Marketing',
    'descripcion': 'Aprende estrategias de marketing digital y tradicional para atraer clientes a tu negocio local.',
    'imagen': 'marketing_local.jpg',
    'estrellas': round(random.uniform(4.3, 4.7), 1),
    'precio': random.randint(50, 130),
    'duracion': '17 horas',
    'estudiantes': random.randint(9000, 16000),
    'ultima_actualizacion': '06/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, casos prácticos, asesoría personalizada',
    'lo_que_aprenderas': [
        'Fundamentos de marketing local.',
        'Publicidad en redes sociales y offline.',
        'Gestión de clientes y reputación.',
        'Promociones y fidelización.',
        'Medición y análisis de resultados.'
    ],
    'requisitos': [
        'Interés en marketing y ventas.',
        'Propietarios o administradores de negocios.',
        'Acceso a computadora o móvil.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '17 horas',
        'detalle': [
            'Introducción al marketing local.',
            'Publicidad digital y offline.',
            'Gestión de clientes.',
            'Promociones y fidelización.',
            'Análisis y mejora.'
        ]
    }
},
{
    'id': 31,
    'titulo': 'Curso Básico de Photoshop para Diseño Gráfico',
    'categoria': 'Diseño',
    'descripcion': 'Aprende las herramientas esenciales de Photoshop para crear y editar imágenes profesionales.',
    'imagen': 'photoshop.jpg',
    'estrellas': round(random.uniform(4.5, 4.9), 1),
    'precio': random.randint(50, 130),
    'duracion': '18 horas',
    'estudiantes': random.randint(11000, 20000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, ejercicios prácticos, recursos descargables',
    'lo_que_aprenderas': [
        'Herramientas básicas y avanzadas de Photoshop.',
        'Retoque fotográfico y corrección de color.',
        'Creación de composiciones y montajes.',
        'Diseño para redes sociales y web.',
        'Exportación y formatos de imagen.'
    ],
    'requisitos': [
        'Computadora con Photoshop instalado.',
        'Interés en diseño gráfico.',
        'Ganas de practicar y crear.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '18 horas',
        'detalle': [
            'Introducción a Photoshop.',
            'Herramientas y técnicas.',
            'Retoque y corrección.',
            'Composiciones y montajes.',
            'Proyecto final.'
        ]
    }
},
{
    'id': 32,
    'titulo': 'Curso de Gestión de Proyectos con Metodologías Ágiles',
    'categoria': 'Administración',
    'descripcion': 'Aprende a planificar, ejecutar y controlar proyectos utilizando metodologías ágiles como Scrum y Kanban.',
    'imagen': 'gestion_proyectos.jpg',
    'estrellas': round(random.uniform(4.4, 4.8), 1),
    'precio': random.randint(50, 130),
    'duracion': '19 horas',
    'estudiantes': random.randint(9000, 17000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, casos prácticos, plantillas y herramientas',
    'lo_que_aprenderas': [
        'Fundamentos de gestión de proyectos.',
        'Introducción a metodologías ágiles.',
        'Scrum, Kanban y herramientas digitales.',
        'Planificación y seguimiento de proyectos.',
        'Liderazgo y gestión de equipos.'
    ],
    'requisitos': [
        'Interés en administración y proyectos.',
        'Ganas de aprender metodologías ágiles.',
        'Acceso a computadora o móvil.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '19 horas',
        'detalle': [
            'Gestión de proyectos básica.',
            'Metodologías ágiles.',
            'Herramientas y software.',
            'Planificación y control.',
            'Liderazgo de equipos.'
        ]
    }
},
{
    'id': 33,
    'titulo': 'Curso Básico de AutoCAD para Diseño Técnico',
    'categoria': 'Arquitectura',
    'descripcion': 'Domina las herramientas básicas de AutoCAD para crear planos y diseños técnicos precisos.',
    'imagen': 'autocad.jpg',
    'estrellas': round(random.uniform(4.5, 4.8), 1),
    'precio': random.randint(50, 130),
    'duracion': '20 horas',
    'estudiantes': random.randint(7000, 14000),
    'ultima_actualizacion': '07/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, ejercicios prácticos, recursos descargables',
    'lo_que_aprenderas': [
        'Interfaz y comandos básicos de AutoCAD.',
        'Creación de planos técnicos.',
        'Uso de capas y bloques.',
        'Impresión y exportación de planos.',
        'Buenas prácticas en diseño técnico.'
    ],
    'requisitos': [
        'Interés en diseño y arquitectura.',
        'Computadora con AutoCAD instalado.',
        'Ganas de practicar y aprender.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '20 horas',
        'detalle': [
            'Introducción a AutoCAD.',
            'Herramientas básicas.',
            'Diseño y planos.',
            'Impresión y exportación.',
            'Proyecto final.'
        ]
    }
},
{
    'id': 34,
    'titulo': 'Curso de Ventas y Técnicas de Negociación',
    'categoria': 'Administración',
    'descripcion': 'Mejora tus habilidades de venta y aprende técnicas efectivas de negociación para cerrar más negocios.',
    'imagen': 'ventas.jpg',
    'estrellas': round(random.uniform(4.4, 4.8), 1),
    'precio': random.randint(50, 130),
    'duracion': '18 horas',
    'estudiantes': random.randint(8000, 15000),
    'ultima_actualizacion': '06/2025',
    'idioma': 'Español',
    'acceso': 'Acceso de por vida en dispositivos móviles y TV',
    'beneficios': 'Certificado, casos prácticos, ejercicios interactivos',
    'lo_que_aprenderas': [
        'Fundamentos de ventas efectivas.',
        'Técnicas de persuasión y cierre.',
        'Manejo de objeciones.',
        'Negociación y trato con clientes.',
        'Seguimiento y fidelización.'
    ],
    'requisitos': [
        'Interés en ventas y negocios.',
        'Ganas de practicar y mejorar.',
        'Acceso a computadora o móvil.'
    ],
    'contenido_curso': {
        'secciones': 5,
        'clases': 19,
        'duracion_total': '18 horas',
        'detalle': [
            'Introducción a ventas.',
            'Técnicas de persuasión.',
            'Negociación efectiva.',
            'Manejo de objeciones.',
            'Seguimiento y fidelización.'
        ]
    }
},






]

@app.route('/')
def index():
    return render_template('index.html', cursos=cursos)

from datetime import datetime

@app.route('/curso/<int:id>')
def curso(id):
    curso_seleccionado = next((c for c in cursos if c['id'] == id), None)
    if not curso_seleccionado:
        return "Curso no encontrado", 404
    # PASAMOS cursos para recomendados y now para el año actual
    return render_template('curso.html', curso=curso_seleccionado, cursos=cursos, now=datetime.now())



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
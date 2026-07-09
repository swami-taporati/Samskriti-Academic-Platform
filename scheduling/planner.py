from scheduling.schedule_factory import create_schedule
from scheduling.allocator import Allocator
from scheduling.exporter import ExcelExporter
from scheduling.exporters.timetable_exporter import TimetableExporter

def generate_empty_schedule(masters, academic_year, division, level, term):
    return create_schedule(
        masters=masters,
        academic_year=academic_year,
        division=division,
        level=level,
        term=term,
    )

def generate_allocated_schedule(masters, academic_year, division, level, term):
    schedule = generate_empty_schedule(
        masters, academic_year, division, level, term
    )
    return Allocator().allocate(schedule, masters)

def export_allocated_schedule(result, output_file:str):
   TimetableExporter().export(result.schedule,output_file,)    
   return output_file

class Spell():
    def __init__(self, pk, name, level, casting_time, spell_range, components, duration, description, higher_level, ritual, concentration, school, material, spell_class):
        self.pk = pk
        self.name = name
        self.level = level
        self.castingTime = casting_time
        self.range = spell_range
        self.components = components
        self.duration = duration
        self.description = description
        self.higherLevel = higher_level
        self.ritual = ritual
        self.concentration = concentration
        self.school = school
        self.material = material
        self.spellClass = spell_class

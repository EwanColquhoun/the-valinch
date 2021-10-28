from django.contrib import admin
from django import forms
from .models import Booking, Aircraft, Slot


@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    """
    Manages Aircraft
    """
    list_filter = ('reg', 'desc',)
    list_display = ('reg', 'desc',)
    search_fields = ['reg', ]


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    """
    Manages Slot allocation
    """
    class Meta:
        ordering = ['start']
        fields = ('start', 'duration', )
        widgets = {
            'start': forms.TimeInput(format='%H:%M'),
            'duration': forms.TimeInput(format='%H'),
        }
    list_filter = ('slot', 'start')
    list_display = ('slot', 'start')
    search_fields = ['slot', 'start']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Manages bookings
    """
    class Meta:
        model = Booking
        widgets = {
          'notes': forms.Textarea(attrs={'rows': 5, 'cols': 33}),
        }

    list_filter = ('date', 'aircraft', 'username', 'instructor_requested', 'approved')
    list_display = ('date', 'slot', 'aircraft', 'username', 'instructor_requested', 'created_on', 'notes', 'approved')
    search_fields = ['date', 'aircraft', 'username', 'instructor_requested']
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)

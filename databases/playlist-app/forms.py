"""Forms for playlist app."""

from wtforms import SelectField, StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField('Playlist Name', validators=[InputRequired(), Length(max=40)])
    description = StringField('Description', validators=[InputRequired(), Length(max=200)])
    submit = SubmitField('Add New Playlist')

class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField('Title', validators=[InputRequired, Length(30)])
    artist = StringField('Artist', validators=[InputRequired(), Length(30)])

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)

select 
  'Arabic     : '|| unistr( '\0627\0644\0639\0631\0628\064A\0629' )      || '
  Chinese    : ' || unistr( '\4E2D\6587' )                               || '
  English    : ' || unistr( 'English' )                                  || '
  French     : ' || unistr( 'Fran\00E7ais' )                             || '
  German     : ' || unistr( 'Deutsch' )                                  || '
  Greek      : ' || unistr( '\0395\03BB\03BB\03B7\03BD\03B9\03BA\03AC' ) || '
  Hebrew     : ' || unistr( '\05E2\05D1\05E8\05D9\05EA' )                || '
  Japanese   : ' || unistr( '\65E5\672C\8A9E' )                          || '
  Korean     : ' || unistr( '\D55C\AD6D\C5B4' )                          || '
  Portuguese : ' || unistr( 'Portugu\00EAs' )                            || '
  Russian    : ' || unistr( '\0420\0443\0441\0441\043A\0438\0439' )      || '
  Spanish    : ' || unistr( 'Espa\00F1ol' )                              || '
  Thai       : ' || unistr( '\0E44\0E17\0E22' )
  as unicode_test_string
from dual ;
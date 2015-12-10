
function typeIt($id, $text, $delay, $cursorCount)
{  
  var flashSpeed = 400;  

  for (var i = 0; i < $cursorCount * 2; i+=2)
  {
    window.setTimeout("$('" + $id + "').html('|')",   (i)     * flashSpeed);
    window.setTimeout("$('" + $id + "').html('_')",    (i + 1) * flashSpeed);
  }


  window.setTimeout("addLetter('" + $id + "','" + $text + "'," +$delay +" ,1); ", $cursorCount * 2 * flashSpeed);

}

//Adds a single letter then recurses back on itself on a timer
function addLetter($id, $text, $delay, $i)
{  
  var $textToSet = $text.substring(0,$i);
  if ($textToSet != $text)
  {    
    $($id).html($textToSet);
    window.setTimeout(function(){addLetter($id, $text,$delay, $i+1)},$delay);
  }
  else
  {
    $($id).html($textToSet);    
  }  
}

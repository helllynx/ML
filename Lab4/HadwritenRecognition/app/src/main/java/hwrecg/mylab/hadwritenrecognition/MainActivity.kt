package hwrecg.mylab.hadwritenrecognition

import android.app.Activity
import android.content.Context
import android.graphics.*
import android.os.Bundle
import android.view.View
import android.widget.RelativeLayout
import android.widget.RelativeLayout.LayoutParams.*
import kotlinx.android.synthetic.main.activity_main.*
import android.graphics.Bitmap
import android.view.MotionEvent
import android.graphics.Bitmap.CompressFormat
import java.io.*
import java.net.Socket
import android.util.Log
import org.jetbrains.anko.*
import java.nio.ByteBuffer
import java.nio.file.Files.size




class MainActivity : Activity() {

    var canvas: Canvas? = null
    var paint: Paint = Paint()
    var view: View? = null
    var path: Path = Path()
    var bitmap: Bitmap? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val pathToFile = getExternalFilesDir(null).absolutePath + "/image.png"

        view = SketchSheetView(this)

        releativeLayout.addView(view, RelativeLayout.LayoutParams(
                1200,
                1200))
        (view as SketchSheetView).isDrawingCacheEnabled = true
        paint.isDither = true
        paint.color = Color.parseColor("#000000")
        paint.style = Paint.Style.STROKE
        paint.strokeJoin = Paint.Join.ROUND
        paint.strokeCap = Paint.Cap.ROUND
        paint.strokeWidth = 100F

        val image = File(pathToFile)
        image.createNewFile()

        button_clear.setOnClickListener { path.reset()
            (view as SketchSheetView).destroyDrawingCache()}
        button_save.setOnClickListener {
            val b = (view as SketchSheetView).drawingCache
            val file = FileOutputStream(image)
            b.compress(CompressFormat.PNG, 100, file)
            sendFile(image, "195.9.98.82", 12480)

            (view as SketchSheetView).destroyDrawingCache()
        }

    }

    internal inner class SketchSheetView(context: Context) : View(context) {

        private val drawingClassArrayList = ArrayList<DrawingClass>()

        init {
            bitmap = Bitmap.createBitmap(1200, 1200, Bitmap.Config.ARGB_8888)
            canvas = Canvas(bitmap)
            this.setBackgroundColor(Color.WHITE)
        }

        override fun onTouchEvent(event: MotionEvent): Boolean {

            val pathWithPaint = DrawingClass()

            canvas?.drawPath(path, paint)

            if (event.action == MotionEvent.ACTION_DOWN) {
                path.moveTo(event.x, event.y)
                path.lineTo(event.x, event.y)
            } else if (event.action == MotionEvent.ACTION_MOVE) {
                path.lineTo(event.x, event.y)
                pathWithPaint.path = path
                pathWithPaint.paint = paint
                drawingClassArrayList.add(pathWithPaint)
            }

            invalidate()
            return true
        }

        override fun onDraw(canvas: Canvas) {
            super.onDraw(canvas)
            if (drawingClassArrayList.size > 0) {

                canvas.drawPath(
                        drawingClassArrayList[drawingClassArrayList.size - 1].path,
                        drawingClassArrayList[drawingClassArrayList.size - 1].paint)
            }
        }
    }

    inner class DrawingClass {

        var path: Path? = null
        var paint: Paint? = null
    }

    fun sendFile(file: File, host: String, port: Int){
        doAsync {
            try {
                val socket = Socket(host, port)
                val outputStream = socket.getOutputStream()

                val fis = FileInputStream(file)

                val buffer = ByteArray(1448)
                val byteArrayOutputStream = ByteArrayOutputStream()

                while (fis.read(buffer) > 0) {
                    byteArrayOutputStream.write(buffer)
                }

                val size = ByteBuffer.allocate(4).putInt(byteArrayOutputStream.size()).array()
                outputStream.write(size)
                outputStream.write(byteArrayOutputStream.toByteArray())
                outputStream.flush()

                val sio = socket.getInputStream()
                val b = sio.read()
                socket.close()

                runOnUiThread {
//                    alert(b.toString())
//                    toast(b.toString())

                    alert("You number is ${b} - it is correct?") {
                        title = "Recognition"
                        yesButton { toast("Yess!!!") }
                        noButton { toast("Sorry =(")}
                    }.show()
                }

            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

}



